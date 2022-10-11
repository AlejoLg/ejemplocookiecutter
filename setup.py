#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
HtmlTestRunner
===============================


.. image:: https://img.shields.io/pypi/v/ejemplocookiecutter.svg
        :target: https://pypi.python.org/pypi/ejemplocookiecutter
.. image:: https://img.shields.io/travis/Alejo_Lg/ejemplocookiecutter.svg
        :target: https://travis-ci.org/Alejo_Lg/ejemplocookiecutter

Python Boilerplate contains all the boilerplate you need to create a Python package.


Links:
---------
* `Github <https://github.com/Alejo_Lg/ejemplocookiecutter>`_
"""

from setuptools import setup, find_packages

requirements = ['Click>=6.0', ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Alejo Legname",
    author_email='alegname@leafnoise.io',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    entry_points={
        'console_scripts': [
            'ejemplocookiecutter=ejemplocookiecutter.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=__doc__,
    include_package_data=True,
    keywords='ejemplocookiecutter',
    name='ejemplocookiecutter',
    packages=find_packages(include=['ejemplocookiecutter']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Alejo_Lg/ejemplocookiecutter',
    version='0.1.0',
    zip_safe=False,
)
