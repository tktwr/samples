#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.argparse*

import sys
import argparse


def parse_args(argv):
    parser = argparse.ArgumentParser(description='description')
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='show verbose message')
    parser.add_argument('-s', '--str',
                        type=str,
                        default="str",
                        help='set str')
    parser.add_argument('-i', '--int',
                        type=int,
                        default=1,
                        help='set int')
    parser.add_argument('-f', '--float',
                        type=float,
                        default=1.0,
                        help='set float')

    args = parser.parse_args()
    return args


def main(argv):
    print(argv)

    args = parse_args(argv)
    print(f"args.verbose: {args.verbose}")
    print(f"args.str: {args.str}")
    print(f"args.int: {args.int}")
    print(f"args.float: {args.float}")


if __name__ == "__main__":
    main(sys.argv)

