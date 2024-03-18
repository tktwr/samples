#!/bin/bash

#======================================================
# variables
#======================================================
APPS="\
sample_c++11 \
sample_c++14 \
sample_c++17 \
sample_c++20 \
sample_class \
sample_cstdio \
sample_fstream \
sample_hello_world \
sample_move \
sample_stl \
sample_stream \
sample_string \
sample_syntax \
sample_template \
sample_thread \
sample_util \
"

#======================================================
# functions
#======================================================
f_cmake()              { mycmake.sh; }
f_cmake_build()        { mycmake-build.sh; }
f_cmake_clean_build()  { rm -rf _build.*; }
f_cmake_clean_output() { rm -rf _output; }

f_cmake_clean_all() {
  f_cmake_clean_build
  f_cmake_clean_output
}

f_run() {
  for i in $APPS; do
    echo "--- [$i] ---"
    $MY_BUILD_DIR/$i
  done
}

#======================================================
# main
#======================================================
f_fzf_main "$@"

