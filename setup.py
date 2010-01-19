#!/usr/bin/env python
"""
License: BSD

(c) 2009 ::: Robert Corsaro (doki_pen@doki-pen.org)
"""

from setuptools import setup, find_packages

setup(
    name='TracXspfPlugin',
    version='0.11',
    license='BSD',
    author='Robert Corsaro',
    author_email='doki_pen@doki-pen.org',
    url='http://github.com/dokipen',
    description='Xspf flash mp3 player macros',
    zip_safe=True,
    packages=['tracxspf'],
    package_data={
        'tracxspf': ['templates/*.html', 'htdocs/*.swf']
    },
    entry_points={
        'trac.plugins': [
            'tracxspf.macros = tracxspf.macros',
            'tracxspf.web_ui = tracxspf.web_ui',
        ]
    },
)
