#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
from collections import namedtuple

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

setup(
    name="ctx_to_zooniverse",
    version="0.1.0",
    description="Code to support the ingestion of MRO CTX data into the Zooniverse Citizen Science system.",
    long_description=readme + "\n\n" + history,
    author="K.-Michael Aye",
    author_email="kmichael.aye@gmail.com",
    url="https://github.com/michaelaye/ctx_to_zooniverse",
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={"console_scripts": ["ctx_to_zooniverse=ctx_to_zooniverse.cli:main"]},
    package_dir={"ctx_to_zooniverse": "ctx_to_zooniverse"},
    include_package_data=True,
    install_requires=[
        'Click>=6.0', 
        'pandas'
    ],
    license="MIT license",
    zip_safe=False,
    keywords="ctx_to_zooniverse",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    test_suite="tests",
    tests_require=['pytest'],
    setup_requires=["pytest-runner"],
)
