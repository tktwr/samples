#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tt_util as ut
from sample_sys import *
from sample_syntax import *
from sample_dict import *
from sample_list import *
from sample_class import *


if __name__ == '__main__':
    func_lst = ut.get_all_funcs(globals().keys())
    for func in func_lst:
        ut.log_title(f' [{func}] ')
        eval(f'{func}()')
