#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

def foo():
    print('menu1!')

def bar():
    print('menu2!')
    
def baz():
    print('help!')

if __name__ == '__main__':
    
    root = Tk()

    menubar = Menu(root)
    # File Menu
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label='Menu1', command=foo)
    filemenu.add_command(label='Menu2', command=bar)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=quit)
    # Help
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label='Help', command=baz)
    
    # Add
    menubar.add_cascade(label='File', menu=filemenu)
    menubar.add_cascade(label='Help', menu=helpmenu)
    
    root.config(menu=menubar)

    root.title('Menu1')
    root.minsize(300,150)
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.grid()
    
    frame1 = ttk.Frame(root)
    frame1.rowconfigure(0, weight=1)
    frame1.columnconfigure(0,weight=1)
    frame1.grid(sticky=(N,E,S,W))
        
    root.mainloop()
