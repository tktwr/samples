#!/bin/bash

#======================================================
# variables
#======================================================

#======================================================
# functions
#======================================================
f_all() {
  ./main.py
}

f_print() {
  ./main.py f_print
}

f_clean_n() {
  clean-fdfind.sh --output-dir
  clean-fdfind.sh --pycache-dir
}

f_clean() {
  clean-fdfind.sh --output-dir -rm
  clean-fdfind.sh --pycache-dir -rm
}

#======================================================
# main
#======================================================
f_fzf_main "$@"
