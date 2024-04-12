from fontTools.ufoLib import UFOReader
import os

def get_font_version(ufo_path):
    reader = UFOReader(ufo_path)
    info = reader._readInfo(validate=False)
    return info["versionMajor"], info["versionMinor"]

inter_numeric_Regular_path = "fonts-temp/master-ufo/InterNumeric-Regular.ufo"
version_major, version_minor = get_font_version(inter_numeric_Regular_path)

try:
    os.remove("version1.txt")
except FileNotFoundError:
    pass

with open("version.txt", "w") as version_file:
    version_file.write(f"{version_major}.{version_minor:03}")