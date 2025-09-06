#!/bin/bash

source cmd_proj.sh

#======================================================
# functions
#======================================================
f_tags() {
  memotags.sh 'memo:' $(fdfind -e cpp -e py -e vim -e sh -e bat) > tags.memo
  ctags -o tags -R py
}

#======================================================
# main
#======================================================
f_fzf_default() { f_tags; }
f_fzf_main "$@"
