#!/bin/bash

#======================================================
# variables
#======================================================

#======================================================
# functions
#======================================================
f_run() {
  print_versions.py
  sample_argparse.py
  sample_json.py
  sample_matplotlib.py
  sample_os.py
  sample_string.py
  sample_syntax.py
  sample_text.py
}

f_run_ext() {
  sample_kivy.py
  sample_skimage.py
}

f_clean() {
  myclean.sh -rm -py
}

#------------------------------------------------------
f_help() {
  echo "run"
  echo "clean"
  echo "help"
}

f_default() {
  f_help
}

#======================================================
# main
#======================================================
func_name=${1:-"default"}
shift
eval "f_$func_name $@"