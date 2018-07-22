.PHONY: memotags tags
memotags:
	memotags.sh cpp/*.cpp opencv/*.cpp py/*.py > memotags

tags:
	ctags -R cpp util lib
