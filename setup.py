from distutils.core import setup
import py2exe

##setup(console=['C:\Users\Kristopher\Desktop\GeoTagScripts\exifScript.py'])

setup(
    console = [{
            "script":"C:\Users\Kristopher\Desktop\GeoTagScripts\Geo Tag Script.py",
            "icon_resources": [(1, "C:\Users\Kristopher\Desktop\GeoTagScripts\Map-Marker.ico")],
			
            }],
)