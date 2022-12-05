#!/usr/bin/env python3
# coding: utf-8

import io
import os
import glob

from setuptools import find_packages, setup

# name of package CBn Crystal Analysis V1

#Package meta-data
DESCRIPTION= \
""" Python package for analyzing CBn crystal structures automatically. """
URL = "https://github.com/harmslab/CBn_Crystal_Analysis_V1"  # temp URL
EMAIL = "mshavlik@uoregon.edu"
AUTHOR = "Michael Shavlik"
REQUIRES_PYTHON = ">=3.7.0"
VERSION = "1.0.0"

here = os.path.abspath(os.path.dirname(__file__))

# Import README for description
with io.open(os.path.join(here,'README.md'),encoding='utf-8') as f:
    full_description = '\n' + f.read()

    
# Now the part where we do setup?
setup(
    name='CBn-Crystal-Analysis-V1',
    version='1.0.0',
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=full_description,
    url=URL,
    license='MIT',
    packages=['CBn_analysis'],
    scripts=glob.glob("CBn_analysis/execute*.py"),
    keywords='CBn; Crystal structure',
    classifiers = ["Development Status :: 3 - Alpha",
                  'Intended Audience :: Science/Research',
                  'Programming Language :: Python :: 3.7'
                  'Programming Language :: Python :: 3.8',
                  'Programming Language :: Python :: 3.9',
                  'Programming Language :: Python :: 3.10'])