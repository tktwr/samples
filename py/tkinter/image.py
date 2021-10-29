#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter
import cv2
from PIL import Image, ImageTk

root = tkinter.Tk()
root.title("Show Image from OpenCV in Tkinter canvas")

image_bgr = cv2.imread("../../data/sample.jpg")
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB) # imreadはBGRなのでRGBに変換
image_pil = Image.fromarray(image_rgb) # RGBからPILフォーマットへ変換
image_tk  = ImageTk.PhotoImage(image_pil) # ImageTkフォーマットへ変換

h, w = image_bgr.shape[:2]
canvas = tkinter.Canvas(root, width=w, height=h) # Canvas作成
canvas.pack()
canvas.create_image(0, 0, image=image_tk, anchor='nw') # ImageTk 画像配置

root.mainloop()
