TAGS_DIR="\
cpp/*.cpp \
cpp_lib/*.cpp \
opencv/*.cpp \
py/*.py \
py/cv/*.py \
py/numpy/*.py \
vim/*.vim \
sh/*.sh \
bat/*.bat \
"

tags_memo:
	memotags.sh $(TAGS_DIR) > tags.memo

all:
	cd cpp && make all
	cd cpp_lib && make all

clean_n:
	myclean.sh -py
	myclean.sh -b
	myclean.sh -o

