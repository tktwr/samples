#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


if __name__ == '__main__':
    d = {'aa': 1, 'bb': 2}

    s = json.dumps(d)
    print(f'{s} {type(s)}')

    d = json.loads(s)
    print(f'{d} {type(d)}')
