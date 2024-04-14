from fontTools.ttLib.woff2 import compress

"""
    Compress TrueType font to WOFF2 format
"""

ttf_path = 'fonts/variable/InterNumeric[wght,RDNS].ttf'
woff2_path = 'fonts/variable/InterNumeric[wght,RDNS].woff2'

if __name__ == "__main__":
    compress(ttf_path, woff2_path)
