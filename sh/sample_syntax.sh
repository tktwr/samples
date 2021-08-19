#!/bin/sh
# *memo_sh.syntax*

# *memo_sh.syntax.while*
f_while() {
  end=$1
  i=0
  while [ $i -lt $end ]; do
    echo $i
    i=`expr $i + 1`
  done
}

# *memo_sh.syntax.if_z*
f_if_z() {
  if [ -z "$X0" ]; then
    echo "ok"
  fi

  X1=""
  if [ -z "$X1" ]; then
    echo "ok"
  fi

  X2="x2"
  if [ -z "$X2" ]; then
    echo "false"
  else
    echo "ok"
  fi
}

# *memo_sh.syntax.if*
f_if() {
  if [ $1 ]; then
    echo "if"
  elif [ $1 ]; then
    echo "elif"
  else
    echo "else"
  fi
}

#f_case() {
  #case i in $*
  #*word1|*word2)
    #;;
  #esac
#}

f_main() {
  f_while 5
  f_if_z
  f_if 0
  f_if 1
}

f_main

