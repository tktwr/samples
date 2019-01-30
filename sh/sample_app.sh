#!/bin/sh
# *memo_sh.app*

bin_name=`basename $0`

files=""
opt1=0
opt2=""

f_help() {
  echo "NAME"
  echo "  $bin_name"
  echo
  echo "SYNOPSIS"
  echo "  $bin_name [options]"
  echo
  echo "OPTIONS"
  echo "  -h, --help       print help"
  echo "  --opt1           opt1"
  echo "  --opt2=<string>  opt2"
}

f_args() {
  for i in $*; do
    case $i in
      -h|--help)
        f_help
        exit
        ;;
      --opt1)
        opt1=1
        ;;
      --opt2=*)
        opt2=${i#--opt2=}
        ;;
      *)
        files="$files $i"
        ;;
    esac
  done
}

f_args $*

echo $files
echo $opt1
echo $opt2

