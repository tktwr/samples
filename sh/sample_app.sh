#!/bin/sh
# *memo:sample:sh.app*

BIN_NAME=`basename $0`
#------------------------------------------------------
# default values
#------------------------------------------------------
args_files=""
args_opt1=0
args_opt2=""
#------------------------------------------------------
# functions
#------------------------------------------------------
f_help() {
  echo "NAME"
  echo "  $BIN_NAME"
  echo
  echo "SYNOPSIS"
  echo "  $BIN_NAME [options]"
  echo
  echo "OPTIONS"
  echo "  -h, --help       print help"
  echo "  --opt1           opt1"
  echo "  --opt2=<string>  opt2"
}
#------------------------------------------------------
f_parse_args() {
  for i in "$@"; do
    case $i in
      -h|--help) f_help; exit ;;
      --opt1)    args_opt1=1 ;;
      --opt2=*)  args_opt2=${i#--opt2=} ;;
      *)         args_files="$args_files $i" ;;
    esac
  done
}
#------------------------------------------------------
# main
#------------------------------------------------------
f_parse_args "$@"
echo $args_files
echo $args_opt1
echo $args_opt2
