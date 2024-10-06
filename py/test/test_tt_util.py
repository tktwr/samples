#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tt_util as tu


OUTPUT_DIR = '_output'

lines = tu.read_text('input.txt')
tu.write_text(f'{OUTPUT_DIR}/output.txt', lines)

json_data = tu.read_json('input.json')
tu.write_json(f'{OUTPUT_DIR}/output.json', json_data)
