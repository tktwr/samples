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
    parser.add_argument('--str',
                        type=str,
                        default="str",
                        help='set str')
    parser.add_argument('--int',
                        type=int,
                        default=1,
                        help='set int')
    parser.add_argument('--float',
                        type=float,
                        default=1.0,
                        help='set float')
    parser.add_argument('--choice',
                        choices=['choice1', 'choice2', 'choice3'],
                        type=str,
                        default="choice1",
                        help='set choice (default=choice1)')
    parser.add_argument('-t', '--dtype',
                        choices=['uint8', 'uint16', 'float32'],
                        type=str,
                        default="uint8",
                        help='set dtype (default=uint8)')
    parser.add_argument('-s', '--size',
                        nargs='+',
                        type=int,
                        default=[256, 256],
                        help='set image size (default=256 256)')
    parser.add_argument('-c', '--color',
                        nargs='+',
                        type=float,
                        default=[1.0, 1.0, 1.0],
                        help='set color (default=1.0 1.0 1.0)')
    parser.add_argument('file', nargs='*')

    args = parser.parse_args()
    return args


def main(argv):
    print(argv)

    args = parse_args(argv)
    print(f"args.verbose : {args.verbose}")
    print(f"args.str     : {args.str}")
    print(f"args.int     : {args.int}")
    print(f"args.float   : {args.float}")
    print(f"args.choice  : {args.choice}")
    print(f"args.dtype   : {args.dtype}")
    print(f"args.size    : {args.size}")
    print(f"args.color   : {args.color}")
    print(f"args.file    : {args.file}")


if __name__ == "__main__":
    main(sys.argv)
