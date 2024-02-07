#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--str' , type=str , default='str' , help='set str')
    parser.add_argument('--int' , type=int , default=1     , help='set int')
    return parser.parse_args()


print(parse_args())
