#!/usr/bin/env python
# -*- coding: utf-8 -*-

counter = 0


def increment():
    global counter
    counter += 1


print(f'{counter}')

increment()
print(f'{counter}')

increment()
print(f'{counter}')
