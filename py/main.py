#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tt_util as ut
from sample_syntax import *
from sample_syntax_dict import *
from sample_syntax_list import *


if __name__ == '__main__':
    func_lst = ut.get_all_funcs(globals().keys())
    for func in func_lst:
        ut.log_title(f' [{func}] ')
        eval(f'{func}()')
