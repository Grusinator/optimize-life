#!/usr/bin/env python

from distutils.core import setup

with open("README", 'r') as f:
      long_description = f.read()

setup(name='optimize-life',
      version='0.0.1',
      description='Various optimizations in real life like economy etc, with panel app',
      long_description=long_description,
      author='William Sandvej Hansen',
      author_email='grusinator@gmail.com',
      url='https://github.com/Grusinator/optimize-life',
      packages=['panel'],
      )
