#!/usr/bin/env python
# coding: utf-8

import os
import sys

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
	name='appie',
	version='0.0.1',
	description='A Python library for the (hidden) AH rest interface',
	long_description=open('README.rst').read() + '\n\n' +
                     open('HISTORY.rst').read(),
	license=open("LICENSE").read(),
	author="Geoffrey Lehée",
	author_email="geoffrey@lehee.name",
	url='https://github.com/socketubs/Pyping/',
	keywords="ping icmp network latency",
	packages = ['pyping'],
	scripts=["bin/pyping"]
)
