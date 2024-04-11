import shutil, os

# Paths to the UFOs
inter_numeric_Light_path = "fonts-temp/master-ufo/InterNumeric-Light.ufo"
inter_numeric_Regular_path = "fonts-temp/master-ufo/InterNumeric-Regular.ufo"
inter_numeric_Black_path = "fonts-temp/master-ufo/InterNumeric-Black.ufo"

inter_numeric_LightSoftened_path = "fonts-temp/master-ufo/InterNumeric-LightSoftened.ufo"
inter_numeric_Softened_path = "fonts-temp/master-ufo/InterNumeric-Softened.ufo"
inter_numeric_BlackSoftened_path = "fonts-temp/master-ufo/InterNumeric-BlackSoftened.ufo"

inter_numeric_LightRounded_path = "fonts-temp/master-ufo/InterNumeric-LightRounded.ufo"
inter_numeric_Rounded_path = "fonts-temp/master-ufo/InterNumeric-Rounded.ufo"
inter_numeric_BlackRounded_path = "fonts-temp/master-ufo/InterNumeric-BlackRounded.ufo"

kerning_plist = "kerning.plist"

shutil.copy(os.path.join(inter_numeric_Light_path, kerning_plist), 
           os.path.join(inter_numeric_LightSoftened_path, kerning_plist))
shutil.copy(os.path.join(inter_numeric_Light_path, kerning_plist), 
           os.path.join(inter_numeric_LightRounded_path, kerning_plist))

shutil.copy(os.path.join(inter_numeric_Regular_path, kerning_plist), 
           os.path.join(inter_numeric_Softened_path, kerning_plist))
shutil.copy(os.path.join(inter_numeric_Regular_path, kerning_plist), 
           os.path.join(inter_numeric_Rounded_path, kerning_plist))

shutil.copy(os.path.join(inter_numeric_Black_path, kerning_plist), 
           os.path.join(inter_numeric_BlackSoftened_path, kerning_plist))
shutil.copy(os.path.join(inter_numeric_Black_path, kerning_plist), 
           os.path.join(inter_numeric_BlackRounded_path, kerning_plist))