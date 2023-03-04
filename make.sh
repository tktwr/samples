#!/bin/bash

#======================================================
# variables
#======================================================
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

#======================================================
# functions
#======================================================
f_tags_memo() {
  memotags.sh 'sample:' $TAGS_DIR > tags
  mktags_dir.sh
}

f_all() {
  cd cpp && make all
  cd cpp_lib && make all
}

f_clean_n() {
  myclean.sh -py
  myclean.sh -b
  myclean.sh -o
}

#------------------------------------------------------
f_help() {
	echo "tags_memo"
	echo "all"
	echo "clean_n"
	echo "help"
}

f_default() {
  f_tags_memo
}

#======================================================
# main
#======================================================
func_name=${1:-"default"}
shift
eval "f_$func_name $@"
