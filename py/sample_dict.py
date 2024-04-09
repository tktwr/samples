#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tt_util as ut


# *sample:py.dict*
def f_dict():
    d = {
        "aaa": 123,
        "bbb": 234,
        "ccc": 345,
    }

    for key in d:
        print(f"key = {key}")
    print(f"d                     = {d}")
    print(f"d['aaa']              = {d['aaa']}")
    print(f"d.get('aaa')          = {d.get('aaa')}")
    print(f"d.get('zzz')          = {d.get('zzz')}")
    print(f"d.keys()              = {d.keys()}")
    print(f"'aaa' in d            = {'aaa' in d}")
    print(f"'aaa' not in d        = {'aaa' not in d}")
    print(f"d.values()            = {d.values()}")
    print(f"123 in d.values()     = {123 in d.values()}")
    print(f"123 not in d.values() = {123 not in d.values()}")
    print(f"d.pop('aaa')          = {d.pop('aaa')}")
    print(f"d                     = {d}")
    print(f"d.pop('zzz', None)    = {d.pop('zzz', None)}")
    print(f"d                     = {d}")
    print(f"d.clear()             = {d.clear()}")
    print(f"d                     = {d}")


