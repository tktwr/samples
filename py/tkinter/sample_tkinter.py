#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo:sample:py.tkinter*

import sys
import tkinter

root = tkinter.Tk()
root.title("タイトル")
root.geometry("300x300")

# ステータスバーの設定
status = tkinter.Label(root, text="ステータスバー", borderwidth=2, relief="groove")
status.pack(side=tkinter.BOTTOM, fill=tkinter.X)

root.mainloop()
