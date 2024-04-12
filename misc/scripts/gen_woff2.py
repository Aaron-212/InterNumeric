from fontTools.ttLib.woff2 import compress

# Usage example
ttf_path = 'fonts/variable/InterNumeric[wght,RDNS].ttf'
woff2_path = 'fonts/variable/InterNumeric[wght,RDNS].woff2'

# Convert the variable font to WOFF2 format
compress(ttf_path, woff2_path)
