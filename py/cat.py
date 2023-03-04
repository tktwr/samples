#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *sample:py.fileinput*

import argparse
import fileinput


def print_file(fp):
    for line in fp:
        print(line, end='')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args()

    with fileinput.input(args.filenames) as f:
        print_file(f)


if __name__ == "__main__":
    main()
