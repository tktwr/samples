.PHONY: tags tags.memo

tags.memo:
	memotags.sh cpp/*.cpp opencv/*.cpp py/*.py sh/*.sh > tags.memo

tags:
	ctags -R util lib
