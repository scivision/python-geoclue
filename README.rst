.. image:: https://travis-ci.org/scivision/python-geoclue.svg?branch=master
    :target: https://travis-ci.org/scivision/python-geoclue

.. image:: https://coveralls.io/repos/github/scivision/python-geoclue/badge.svg?branch=master
    :target: https://coveralls.io/github/scivision/python-geoclue?branch=master

.. image:: https://api.codeclimate.com/v1/badges/8144d23658b88eb86d20/maintainability
   :target: https://codeclimate.com/github/scivision/python-geoclue/maintainability
   :alt: Maintainability

==============
python-geoclue
==============

Uses available sources of geolocation, including GPS, WiFi BSSID (via Mozilla Location Services), with fallback to IP city-level localization.


Acts as a Python API to DBUS `geoclue`.

.. contents::

Build
=======

Prereqs
-------
::

    apt install gcc libdbus-1-dev libdbus-glib-1-dev geoclue geoclue-examples

Location Providers
~~~~~~~~~~~~~~~~~~
You need a location provider.
Here we use Skyhook, but you can select another or several others::

    apt install geoclue-skyhook

Be sure your location providers are working.

* Skyhook: often within 100 meters in urban locations
* Ubuntu GeoIP: within a city or county

Geoclue GUI test program::

    geoclue-test-gui


These don't seem to be working for me.

    geoclue-hostip
    geoclue-plazes




Install::

    pip install -e .
    
    
Errors
======
Assuming ``geoclue-test-gui`` works for you, but you don't get a location with this program, try running this program as root.


Contributions
=============

The resurrection of this program currently requires Python 2.7 and the deprecated `dbus-python` package.
We'd welcome pull requests building to Python 3 compatibility.
The place to start would be with a Python 3 compatibile Python DBUS API.
