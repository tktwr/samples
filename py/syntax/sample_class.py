#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo:sample:py:syntax:class*


class MyClass():
    def __init__(self):
        print(f"MyClass.__init__")
        self.a = {0: 123}

    def __del__(self):
        print(f"MyClass.__del__")

    def f(self, x):
        self.x = x
        print(f"MyClass.f: {x}")

    def g(self):
        print(f"dir: {dir(self)}")
        print(f"hasattr(self, 'x'): {hasattr(self, 'x')}")
        print(f"hasattr(self, 'a'): {hasattr(self, 'a')}")

    def public_method(self):
        pass

    def _protected_method(self):
        pass

    def __private_method(self):
        pass

    class_member = 0

    @classmethod
    def class_method(cls):
        cls.class_member += 1
        print(f"class_method: {cls.class_member}")


def f_class():
    my = MyClass()
    my.f(10)
    my.g()
    MyClass.class_method()
    MyClass.class_method()
    print(f"MyClass.class_member: {MyClass.class_member}")


# -----------------------------------------------------
class MySubClass(MyClass):
    def f(self, x):
        print(f"MySubClass.f: {x}")


def f_subclass():
    my = MySubClass()
    my.f(10)


