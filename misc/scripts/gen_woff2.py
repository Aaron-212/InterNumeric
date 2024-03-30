from fontTools.ttLib.woff2 import compress

# Usage example
otf_path = 'fonts/variable/InterNumeric[wght,rdns].otf'
woff2_path = 'fonts/variable/InterNumeric[wght,rdns].woff2'

# Convert the variable font to WOFF2 format
compress(otf_path, woff2_path)
