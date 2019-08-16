#!/usr/bin/env python
# -*- coding: utf-8 -*
import os
from codecs import open

from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

desc = (
    'A CLI tool to update your requirements.txt file package versions '
    'to be locked/fixed to the latest versions available on PyPI.'
)

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='lock-requirements',
    version='0.1.1',
    packages=find_packages('src', exclude=('tests',)),
    package_dir={'': 'src'},
    description=desc,
    include_package_data=True,
    long_description=readme,
    long_description_content_type='text/markdown',
    zip_safe=False,
    author='Richard O\'Dwyer',
    author_email='richard@richard.do',
    license='Apache 2.0',
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'lock = lock.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
