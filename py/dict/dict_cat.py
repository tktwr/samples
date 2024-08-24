#!/usr/bin/env python
# -*- coding: utf-8 -*-

dict1 = {'a': 'hello', 'b': 'world'}
dict2 = {'a': 'python', 'b': 'programming', 'c': 'abc'}

def dict_cat_and(dict1, dict2):
    print(dict1.keys() & dict2.keys())
    return {key: f'{dict1[key]}, {dict2[key]}' for key in dict1.keys() & dict2.keys()}

def dict_cat_or(dict1, dict2):
    print(dict1.keys() | dict2.keys())
    return {key: f"{dict1.get(key, '')}, {dict2.get(key, '')}" for key in dict1.keys() | dict2.keys()}

print(dict_cat_and(dict1, dict2))
print(dict_cat_or(dict1, dict2))

