#!/bin/bash

f_args1() {
  for i in "$@"; do
    echo "[$i]"
  done
}

# can handle spaces in filename
echo 'args: "$@"'
f_args1 "$@"

# handle all args as one arg
echo 'args: "$*"'
f_args1 "$*"

# cannot handle spaces in filename
echo 'args: $@'
f_args1 $@

# cannot handle spaces in filename
echo 'args: $*'
f_args1 $*
