#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'imageprep'
DESCRIPTION = 'Image Preparation Utilities for Deep Learning'
URL = 'https://github.com/adbeda/imageprep'
EMAIL = 'adbedada@gmail.com'
AUTHOR = 'Adane Bedada'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = 0.3

with open("README.md") as f:
    long_description = f.read()

REQUIRED = [
    'pillow',
    'click',
    'numpy'
]

EXTRA_REQUIRED = {
    'test': ['mock',
             'pytest',
             'pytest-cov',
             'codecov']}

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('data', 'examples')),
    install_requires=REQUIRED,
    extras_require=EXTRA_REQUIRED,
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
