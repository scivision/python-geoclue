#! /usr/bin/env python

req = ['six','dbus-python']

from setuptools import setup,find_packages

VERSION = '0.1.0'
setup(name='Geoclue',
        version=VERSION,
        author=['Paulo Cabido','Michael Hirsch, Ph.D.'],
        author_email=['paulo.cabido@gmail.com','scivision@users.noreply.github.com'],
        url='https://www.github.com/scivision/python-geoclue',
        description='Geoclue python module',
        long_description="""
        Python-Geoclue is an API interface for Geoclue.
        Almost all Geoclue methods are available.

        It uses the Geoclue D-Bus API in order to facilitate Geoclue's use.
        """,
        packages=find_packages(),
        classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
        install_requires=req,
        python_requires='==2.7.*',
        extras_require={'kml':['simplekml','numpy']},
        )
