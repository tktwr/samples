#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

class Win1(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        self.master.geometry("400x400")
        self.master.title("window 1")
        self.create_widgets()

    def create_widgets(self):
        # Button
        self.button_new_win = ttk.Button(self)
        self.button_new_win.configure(text="Open Window 2")
        self.button_new_win.configure(command = self.new_window)
        self.button_new_win.pack()

    #Call back function
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Win2(self.newWindow)



class Win2(tk.Frame):
    def __init__(self,master):

        super().__init__(master)
        self.pack()
        self.master.geometry("300x300")
        self.master.title("window 2")
        self.create_widgets()

    def create_widgets(self):
        # Button
        self.button_quit = ttk.Button(self)
        self.button_quit.configure(text="Close Window 2")
        self.button_quit.configure(command=self.quit_window)
        self.button_quit.pack()

    def quit_window(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    app = Win1(master=root)#Inherit
    app.mainloop()

if __name__ == "__main__":
    main()
