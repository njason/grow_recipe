#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='plant-recipe-schema',
    version='0.3.0',
    author='Jason Biegel',
    license='LICENSE',
    description='Store plant grow recipes in a structured XML format',
    packages=find_packages(exclude=['docs', 'samples', 'tests']),
    install_requires=[
        'lxml==4.1.1',
    ]
)
