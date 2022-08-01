#!/bin/bash

#======================================================
# variables
#======================================================

#======================================================
# functions
#======================================================

f_test_image() {
  mkdir -p _output/image
  cd _output/image && ../../test_image.sh
}

f_test_pathconv() {
  local os_name=$(uname -osr)
  case $os_name in
    *Msys*)
      ./test_pathconv.sh > _output/msys.txt
      ;;
    *WSL*)
      ./test_pathconv.sh > _output/wsl.txt
      ;;
    *)
      ;;
  esac
}

#------------------------------------------------------
f_help() {
  echo "test_image"
  echo "test_pathconv"
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


