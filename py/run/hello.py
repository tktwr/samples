#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time


for i in range(3):
    time.sleep(2)
    print(f'hello {i}')
    sys.stdout.flush()
