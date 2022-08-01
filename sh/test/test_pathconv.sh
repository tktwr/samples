#!/bin/bash

f_test_sh() {
  echo "f_test_sh"
  orig_fname=$1
  unix_fname=$(pathconv.sh unix $orig_fname)
  win_fname=$(pathconv.sh win $orig_fname)

  echo "orig_fname = $orig_fname"
  echo "unix_fname = $unix_fname"
  echo "win_fname  = $win_fname"
}

f_test_py() {
  echo "f_test_py"
  orig_fname=$1
  unix_fname=$(pathconv.py -t unix $orig_fname)
  mixed_fname=$(pathconv.py -t mixed $orig_fname)
  win_fname=$(pathconv.py -t windows $orig_fname)

  echo "orig_fname  = $orig_fname"
  echo "unix_fname  = $unix_fname"
  echo "mixed_fname = $mixed_fname"
  echo "win_fname   = $win_fname"
}

f_test_sh "C:/Users/Takeh/_vimrc"
f_test_py "C:/Users/Takeh/_vimrc"

f_test_sh "C:/Users/Takeh2/_vimrc"
f_test_py "C:/Users/Takeh2/_vimrc"

f_test_sh "$HOME/WinHome/_vimrc"
f_test_py "$HOME/WinHome/_vimrc"

