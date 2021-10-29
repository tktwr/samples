#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

if __name__ == '__main__':
    fruits = ['Apple', 'Banana', 'Grape']

    root = Tk()
    root.title('Combobox 1')

    # Frame
    frame = ttk.Frame(root, padding=10)
    frame.grid()

    # Combobox
    v = StringVar()
    cb = ttk.Combobox(
        frame, textvariable=v, 
        values=fruits, width=10)
    cb.set(fruits[0])
    cb.bind(
        '<<ComboboxSelected>>', 
        lambda e: print('v=%s' % v.get()))
    cb.grid(row=0, column=0)

    # Button
    button1 = ttk.Button(
        frame, text='OK', 
        command=lambda: print('v=%s' % v.get()))
    button1.grid(row=0, column=1)

    root.mainloop()
