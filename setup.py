#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import os
from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'imageprep'
DESCRIPTION = 'Image Preparation Utilities for Deep Learning'
URL = 'https://github.com/adbeda/imageprep'
EMAIL = 'adbedada@gmail.com'
AUTHOR = 'Adane Bedada'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = 0.2

with open("README.md") as f:
    long_description = f.read()

REQUIRED = [
    'pillow',
    'click'
]


here = os.path.abspath(os.path.dirname(__file__))

about = {}
about['__version__'] = VERSION


# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests','examples','data')),
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    entry_points='''
             [console_scripts]
             imageprep=imageprep.imcli:commands
                 ''',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)



# from setuptools import setup
#
# REQUIRED = [
#     'click>=7.0',
#     'Pillow>=6.2.1'
# ]
# setup(
#     name='imageprep',
#     version=0.2,
#     entry_points='''
#         [console_scripts]
#         imageprep=imcli:commands
#         ''',
#     py_modules=['imageprep','imcli'],
#     install_requires=REQUIRED
# )