#!/usr/bin/env python3

from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='newpro',
    version='1.0.0',
    description=' writing projects.',
    long_description=long_description,
    url='https://github.com/awesmubarak/newpro',
    author='Awes Mubarak',
    author_email='awes.mubarak@awesmubarak.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python'
    ],
    keywords='writing markdown pandoc',
    packages=['newpro'],
    entry_points={
        "console_scripts": [
            "newpro=newpro:main",
        ],
    },
)
