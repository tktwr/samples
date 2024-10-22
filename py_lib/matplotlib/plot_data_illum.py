#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo:sample:py_lib:matplotlib:plot_data_illum*

import json
import matplotlib.pyplot as plt


def f_write_json_file(fname, data):
    with open(fname, 'w') as f:
        f.write(json.dumps(data))


def f_read_json_file(fname, name, wl_begin, wl_end, wl_step):
    with open(fname, 'r') as f:
        data = json.load(f)
    spec = data[name]
    x = spec[::2]
    y = spec[1::2]

    i0 = x.index(wl_begin)
    i1 = x.index(wl_end) + 1
    x = x[i0:i1:wl_step]
    y = y[i0:i1:wl_step]

    return (x, y)


def f_plot(json_fname, name):
    x, y = f_read_json_file(json_fname, name, 420, 720, 2)
    fig, ax = plt.subplots()

    data = {}
    data[name] = [x, y]
    print(data)
    f_write_json_file(f'_output/illum_{name}.json', data)

    #ax.plot(x, y, "-")
    ax.bar(x, y, width=10)
    ax.set_xlabel('wavelength')
    ax.set_ylabel('power')
    ax.legend([f'{name}'])
    plt.savefig(f'_output/plot_{name}.png')
    #plt.show()


f_plot("illum.json", "CIE_Illum_A")
f_plot("illum.json", "CIE_Illum_D5000")
f_plot("illum.json", "CIE_Illum_D6500")
f_plot("illum.json", "CIE_Illum_F1")
f_plot("illum.json", "CIE_Illum_F2")
f_plot("illum.json", "CIE_Illum_F3")
f_plot("illum.json", "CIE_Illum_F4")
f_plot("illum.json", "CIE_Illum_F5")
f_plot("illum.json", "CIE_Illum_F6")
f_plot("illum.json", "CIE_Illum_F7")
f_plot("illum.json", "CIE_Illum_F8")
f_plot("illum.json", "CIE_Illum_F9")
f_plot("illum.json", "CIE_Illum_F10")
f_plot("illum.json", "CIE_Illum_F11")
f_plot("illum.json", "CIE_Illum_F12")
