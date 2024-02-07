#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import subprocess


def run(command):
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    while True:
        line = proc.stdout.readline().decode('utf-8', 'replace')
        if line:
            sys.stdout.write(line)
        if not line and proc.poll() is not None:
            break


cmd = ['./hello.py']
run(cmd)
