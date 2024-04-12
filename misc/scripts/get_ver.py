import os
from glyphsLib import GSFont

def get_font_version(glyphspackage_path):
    font = GSFont(glyphspackage_path)

    return f"{font.versionMajor}.{font.versionMinor:03}"

inter_numeric_src_path = "src/InterNumeric.glyphspackage"

try:
    os.remove("version.txt")
except FileNotFoundError:
    pass

with open("version.txt", "w") as version_file:
    version_file.write(get_font_version(inter_numeric_src_path))