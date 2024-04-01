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

build.stamp: init.stamp
	fontmake -g "src/InterNumeric.glyphspackage" -o variable --output-path "fonts/variable/InterNumeric[wght,RDNS].ttf" --filter DecomposeTransformedComponentsFilter
	touch build.stamp

zip: build.stamp
	cp -rf fonts InterNumeric
	zip -r InterNumeric.zip InterNumeric
	rm -rf InterNumeric

test: build.stamp
	fontbakery check-universal fonts/variable/InterNumeric[wght,RDNS].ttf

cleanbuild:
	rm -rf fonts
	rm -rf fonts-temp
	rm build.stamp

cleanufo:
	rm -rf fonts-temp
	rm ufo.stamp

update:
	pip install -Ur requirements.txt
