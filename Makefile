help:
	@echo "###"
	@echo "# Build targets for Inter Numeric"
	@echo "###"
	@echo
	@echo "  make build:  Builds the fonts and places them in the fonts/ directory"
	@echo "  make zip:  Zip all fonts into a zip"
	@echo

init: requirements.txt
	pip install -Ur requirements.txt
	touch init.stamp

build: build.stamp

# fontmake -m "fonts-temp/master-ufo/InterNumeric.designspace" -o variable --output-path "fonts/variable/InterNumeric[wght,ROND].ttf" --filter DecomposeTransformedComponentsFilter --verbose DEBUG
# fontmake -m "fonts-temp/master-ufo/InterNumeric.designspace" -o variable-cff2 --output-path "fonts/variable/InterNumeric[wght,ROND].otf"


build.stamp: init.stamp
	fontmake -g "src/InterNumeric.glyphspackage" -o ufo --output-dir "fonts-temp/master-ufo" --filter DecomposeTransformedComponentsFilter
	python misc/scripts/copy_kern.py
	python misc/scripts/stat.py
	fontmake -m "fonts-temp/master-ufo/InterNumeric.designspace" -o variable --output-path "fonts/variable/InterNumeric[wght,ROND].ttf" --filter DecomposeTransformedComponentsFilter
	python misc/scripts/gen_woff2.py
	touch build.stamp

zip: build.stamp
	cp -rf fonts InterNumeric
	zip -r InterNumeric.zip InterNumeric
	rm -rf InterNumeric


# fontbakery check-googlefonts "fonts/variable/InterNumeric[wght,ROND].ttf"

test: build.stamp
	fontbakery check-universal "fonts/variable/InterNumeric[wght,ROND].ttf" -x com.google.fonts/check/case_mapping

clean:
	rm -rf fonts
	rm -rf fonts-temp
	rm build.stamp

update:
	pip install -Ur requirements.txt
