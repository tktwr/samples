#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from ttkthemes import *

root = ThemedTk()
root.title('My First App')
root.minsize(width=400, height=100)

s = ttk.Style()
s.theme_use('black')

# Create Widgets
frame1 = ttk.Frame(root, padding=10)
label1 = ttk.Label(frame1, text='Your name:')
t = StringVar()
entry1 = ttk.Entry(frame1, textvariable=t)
button1 = ttk.Button(
    frame1,
    text='OK',
    command=lambda: print('Hello, %s.' % t.get()))

# Grid
frame1.grid(row=0, column=0, sticky=(N, W, S, E))
label1.grid(row=0, column=0, sticky=E)
entry1.grid(row=0, column=1, sticky=(E, W))
button1.grid(row=1, column=1, sticky=W)

# Set Padding
for child in frame1.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Set Grid Weight
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame1.columnconfigure(1, weight=1)

# Window Position
root.geometry("+300+200")

# Start App
root.mainloop()
