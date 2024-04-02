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

# fontmake -g "src/InterNumeric.glyphspackage" -o variable --output-path "fonts/variable/InterNumeric[wght,RDNS].ttf" --filter DecomposeTransformedComponentsFilter --verbose DEBUG
# fontmake -g "src/InterNumeric.glyphspackage" -o variable-cff2 --output-path "fonts/variable/InterNumeric[wght,RDNS].otf" --filter DecomposeTransformedComponentsFilter --verbose DEBUG
# fontmake -g "src/InterNumeric.glyphspackage" -o otf --output-dir "fonts/static/" --filter DecomposeTransformedComponentsFilter -i

build.stamp: init.stamp
	fontmake -g "src/InterNumeric.glyphspackage" -o variable --output-path "fonts/variable/InterNumeric[wght,RDNS].ttf" --filter DecomposeTransformedComponentsFilter
	python misc/scripts/stat.py
	touch build.stamp

zip: build.stamp
	cp -rf fonts InterNumeric
	zip -r InterNumeric.zip InterNumeric
	rm -rf InterNumeric

test: build.stamp
	fontbakery check-universal "fonts/variable/InterNumeric[wght,RDNS].ttf"

cleanbuild:
	rm -rf fonts
	rm -rf fonts-temp
	rm build.stamp

cleanufo:
	rm -rf fonts-temp
	rm ufo.stamp

update:
	pip install -Ur requirements.txt
