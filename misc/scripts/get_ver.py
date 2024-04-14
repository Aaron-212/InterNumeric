from glyphsLib import GSFont

"""
    Get font version from Glyphspackage source file, store it in verion.txt
    No need to keep track of version in a seperate file.
    Only used in GitHub Workflows to give artifacts a file name.
"""

def get_font_version(glyphspackage_path):
    font = GSFont(glyphspackage_path)

    return f"{font.versionMajor}.{font.versionMinor:03}"

inter_numeric_src_path = "src/InterNumeric.glyphspackage"

with open("version.txt", "w") as version_file:
    version_file.write(get_font_version(inter_numeric_src_path))