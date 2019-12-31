#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.kivy*

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()
