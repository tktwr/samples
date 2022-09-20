# from distutils.core import setup, Extension
from setuptools import setup, Extension

ext_modules = [
    Extension(
        'myModule',
        sources=['py_hello.c']
    )
]

setup(
    name='myModule',
    version='1.0.1',
    ext_modules=ext_modules
)
