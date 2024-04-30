#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo:sample:py.argparse*

import sys
import argparse


def parse_args(argv):
    choices1      = ['choice1', 'choice2', 'choice3']
    choices2      = ['uint8', 'uint16', 'float32']
    default_size  = [256, 256]
    default_color = [1.0, 1.0, 1.0]

    parser = argparse.ArgumentParser(description='description')

    parser.add_argument('-v'  , '--verbose' , action='store_true' , help='show verbose message')

    parser.add_argument('-s'  , '--str'    , type=str   , default='str'         , help='set str')
    parser.add_argument('-i'  , '--int'    , type=int   , default=1             , help='set int')
    parser.add_argument('-f'  , '--float'  , type=float , default=1.0           , help='set float')
    parser.add_argument('-c'  , '--choice' , type=str   , default='choice1'     , help='set choice (default=choice1)'     , choices=choices1 , )
    parser.add_argument('-dt' , '--dtype'  , type=str   , default='uint8'       , help='set dtype (default=uint8)'        , choices=choices2 , )
    parser.add_argument('-sz' , '--size'   , type=int   , default=default_size  , help='set image size (default=256 256)' , nargs='+'        , )
    parser.add_argument('-co' , '--color'  , type=float , default=default_color , help='set color (default=1.0 1.0 1.0)'  , nargs='+'        , )

    parser.add_argument('-xx'     , type=str , default='str' , help='set str')
    parser.add_argument('--xx-xx' , type=str , default='str' , help='set str')

    parser.add_argument('file', nargs='*')

    return parser.parse_args()


def main(argv):
    print(argv)

    args = parse_args(argv)
    for arg in vars(args):
        print(f'{arg}\t: {getattr(args, arg)}')


if __name__ == '__main__':
    main(sys.argv)
