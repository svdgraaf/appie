#!/usr/bin/env python
# coding: utf-8

import os
import sys

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

if sys.argv[-1] == 'publish':
	import os
	os.system('python setup.py sdist upload')
	sys.exit()

setup(
	name='appie',
	version='0.0.2',
	description='A Python library for the (hidden) AH rest interface',
	setup_requires=['setuptools-markdown'],
	long_description_markdown_filename='README.md',
	license=open("LICENSE").read(),
	author="Sander van de Graaf",
	author_email="mail@svdgraaf.nl",
	url='https://github.com/svdgraaf/appie',
	keywords="ah rest appie albert",
	packages = ['appie'],
)
