#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Button Example')

# Frame as Widget Container
frame1 = ttk.Frame(
    root,
    padding=10)
frame1.grid()

# Label 1
icon = PhotoImage(file='app.png')

label1 = ttk.Label(
    frame1,
    image=icon)
label1.grid(row=0, column=0)

# Label 2
label2 = ttk.Label(
    frame1,
    text='Will schools be open this fall?',
    width=20,
    anchor=W,
    padding=(20))
label2.grid(row=0, column=1)

# ボタン
button1 = ttk.Button(
    frame1,
    text='OK',
    command=lambda: root.quit())
button1.grid(row=1, column=0, columnspan=2)

root.mainloop()
