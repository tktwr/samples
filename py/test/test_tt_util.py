#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import tt_util as tu


O_DIR = '_output'


def f_search():
    s = '/a/$MY_DATA/a/b'
    #s = '$HOME/a/b'
    r = re.search('^\$MY_', s)
    print(r)


