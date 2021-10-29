#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Label Example')

# Frame as widget container
frame1 = ttk.Frame(root)
frame1.grid()

# Image
pencil_image = PhotoImage(file='app.png')

# Label 1
label1 = ttk.Label(
    frame1,
    image=pencil_image)
label1.grid(row=0, column=0)

# Label 2
label2 = ttk.Label(
    frame1,
    text='Will schools be open this fall?',
    padding=(20)) # (left, top, right, bottom)
label2.grid(row=0, column=1)

root.mainloop()
