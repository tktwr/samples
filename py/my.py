# -*- coding: utf-8 -*-

class MyClass():
    n = 0
    def __init__(self, x):
        MyClass.n += 1
        self.x = x
    def add(self, x):
        self.x += x
        return self.x
    @classmethod
    def f(self, text):
        print(text)

class SubClass(MyClass):
    def g(self):
        return self.x

