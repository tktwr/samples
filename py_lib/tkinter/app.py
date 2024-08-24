#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText


def f_open():
    fname = filedialog.askopenfilename() 
    print(f"{fname}")


def f_quit():
    quit()


def f_help():
    print(f"help")


def app(argv):
    root = Tk()

    menubar = Menu(root)

    # File Menu
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label='Open', command=f_open)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=f_quit)

    # Help
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label='Help', command=f_help)
    
    # Add
    menubar.add_cascade(label='File', menu=filemenu)
    menubar.add_cascade(label='Help', menu=helpmenu)
    
    root.config(menu=menubar)

    root.title('App')
    root.minsize(300,150)
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.grid()
    
    frame1 = ttk.Frame(root)
    frame1.rowconfigure(0, weight=1)
    frame1.columnconfigure(0,weight=1)
    frame1.grid(sticky=(N,E,S,W))

    text = "hello world\n"
    text += "hello world\n"
   
    text_field = ScrolledText(frame1)
    text_field.place(x=0, y=0, width=300, height=150)
    text_field.insert(1.0, text)
    #text_field.configure(state='disabled') # disable edit
        
    root.mainloop()


if __name__ == "__main__":
    app(sys.argv)

