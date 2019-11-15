tags: tags.memo

.PHONY: tags.memo
tags.memo:
	memotags.sh cpp/*.cpp cpp_lib/*.cpp opencv/*.cpp py/*.py sh/*.sh bat/*.bat > tags.memo

