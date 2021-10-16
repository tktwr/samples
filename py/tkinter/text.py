#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter.scrolledtext import ScrolledText

# アプリの定義
class ScrollTextFieldApp(tk.Frame):
    # 初期化
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, width=240, height=240)

        # タイトルの表示
        self.master.title('スクロール可能なテキストフィールド')
       
        # テキストの生成
        text = ''
        for i in range(100):
            text += 'あいうえおかきくけこさしすせそたちつてとなにぬねの'
       
        # スクロール可能なテキストフィールドの生成
        text_field = ScrolledText(self)
        text_field.insert(1.0, text)
        text_field.configure(state='disabled') # 編集無効        
        text_field.place(x=0, y=0, width=240, height=240)

# アプリの実行
app = ScrollTextFieldApp()
app.pack()
app.mainloop()
