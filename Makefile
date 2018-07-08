.PHONY: memotags tags
memotags:
	memotags.sh cpp/*.cpp opencv/*.cpp > memotags

tags:
	ctags -R cpp util lib
