#Kristopher Sousa
#Sept 26, 2016
#Outputs GeoTags from a dir containg JPG GIF PNG TIF files in DD format to a .csv

import exifread
import os

##Force Windows Size Constant
os.system("mode con: cols=100 lines=30")

##Ouput Title 
print """
####################################################################################################

					GeoTag to CSV Converter

####################################################################################################
"""

##Functions 
def getGeoTagAsDD(tag, tags):
		strTag = "%s,%s" % (tag, tags[tag])
		##Broken into float parts of dms format
		degrees = float(strTag[strTag.find(",[")+2:strTag.find(", ")])
		minutes = float(strTag[strTag.find(", ")+2:strTag.find(", ",strTag.find(", ")+1)])
		numerator = strTag[strTag.find(", ",strTag.find(", ")+1)+2:strTag.find("/")]
		denominator = strTag[strTag.find("/")+1:strTag.find("]")]
		seconds = float(numerator)/float(denominator)
		
		##Converting to DD format		
		ddFormat = degrees + minutes/60 + seconds/3600
		ddFormat = ddFormat*latSign

		
		return ddFormat

##Inputs path to Dir
path = raw_input("Path to folder or file:" )

##Opens Ouput file
outputPath = os.path.expanduser("~\Desktop\GpsData.csv")
outputFile = open(outputPath, "w")

##Initialize Variables
longSign = 1
latSign = 1
ddLat = 0		
ddLong = 0
longFlag = 0
latFlag = 0

##Main Loop
try:
	if path.endswith(".jpg") or path.endswith(".tif") or path.endswith(".png") or path.endswith(".gif"):
		##Opens Image file
		imgFile = open(path, 'rb')

		##Gets Tags
		tags = exifread.process_file(imgFile)

		##Get Image Name
		imgName = os.path.split(imgFile.name)[1]
		imgName = imgName[:imgName.find(".")]

		##Cycles through Tags to get sign of DD
		for tag in tags.keys():
			if tag == "GPS GPSLongitudeRef":
				if str(tags[tag]) == "W":
					longSign = -1
			if tag == "GPS GPSLatitudeRef":
				if str(tags[tag]) == "S":
					latSign = -1

		##Cycles through Tags to get value of DD than applies DD sign			
		for tag in tags.keys():
			if tag == "GPS GPSLongitude":
				ddLong = getGeoTagAsDD(tag, tags)
				ddLong = ddLong*longSign
				longFlag = 1
			if tag == "GPS GPSLatitude":
				ddLat = getGeoTagAsDD(tag, tags)
				ddLat = ddLat*latSign
				latFlag = 1
		
			##Prevents files without a GeoTag from taking the corridnates of the file before it
			if latFlag == 0 and longFlag == 0:
				ddLong = 0		
				ddLat = 0
		
		##Resets Flags
		longFlag = 0
		latFlag = 0				
		
		##Output
		strOutput = "%s,%s,%s\r" % (imgName,ddLat,ddLong)
		print "%s	%s	%s\r" % (imgName,ddLat,ddLong)
		outputFile.write(strOutput)
		
		##Close Image File
		imgFile.close()
	else:
		##Makes it easier to copy paste from the path
		if path.endswith("\\") == False:
			path = path + "\\"
			print path
		
		
		for filename in os.listdir(path):
			if filename.endswith(".jpg") or filename.endswith(".tif") or filename.endswith(".png") or filename.endswith(".gif"):
				##Opens Image file
				imgFile = open(path+filename, 'rb')

				##Gets Tags
				tags = exifread.process_file(imgFile)

				##Get Image Name
				imgName = os.path.split(imgFile.name)[1]
				imgName = imgName[:imgName.find(".")]

				##Cycles through Tags to get sign of DD
				for tag in tags.keys():
					if tag == "GPS GPSLongitudeRef":
						if str(tags[tag]) == "W":
							longSign = -1
					if tag == "GPS GPSLatitudeRef":
						if str(tags[tag]) == "S":
							latSign = -1

				##Cycles through Tags to get value of DD than applies DD sign			
				for tag in tags.keys():
					if tag == "GPS GPSLongitude":
						ddLong = getGeoTagAsDD(tag, tags)
						ddLong = ddLong*longSign
						longFlag = 1
					if tag == "GPS GPSLatitude":
						ddLat = getGeoTagAsDD(tag, tags)
						ddLat = ddLat*latSign
						latFlag = 1
					
					##Prevents files without a GeoTag from taking the corridnates of the file before it
					if latFlag == 0 and longFlag == 0:
						ddLong = 0		
						ddLat = 0
				
				##Resets Flags
				longFlag = 0
				latFlag = 0				
				
				##Output
				strOutput = "%s,%s,%s\r" % (imgName,ddLat,ddLong)
				print "%s	%s	%s\r" % (imgName,ddLat,ddLong)
				outputFile.write(strOutput)
				
				##Close Image File
				imgFile.close()	
except:
	print"""
Files: Supported types are .jpg, .tif, .png and .gif

Folders: Folder path must have \ seperating path root and at the end

Other: If your pictures are returning 0 0 as their coordinates that is because no GeoTag is present

For other problems please check out the source code file, Sorry - Kris 
	"""

##Closes output file
outputFile.close()		

##Input to prevent file closing
raw_input("\nPress any key to exit.")


##Contact Kristopher Sousa for any issues and I will try and help (Including once I leave HOL using my email kristopher.m.sousa@gmail.com)