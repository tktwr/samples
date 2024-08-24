#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time


for i in range(3):
    print(f'hello {i}')
    sys.stdout.flush()
    time.sleep(2)
