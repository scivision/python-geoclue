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
Here we use `Skyhook <http://www.skyhookwireless.com/Coverage-Map>`_, but you can select another or several other location providers::

    apt install geoclue-skyhook

Be sure your location providers are working.

* ``geoclue-skyhook``: ~ 100 meter accuracy in urban locations
* ``geoclue-ubuntu-geoip``: within a city or county

These don't seem to be working.

    geoclue-hostip
    geoclue-plazes

`Mozilla Location Services <https://location.services.mozilla.com/map>`_ are also usable in Geoclue.


Install
-------
::

    pip install -e .


Run
---
Currently Python 2.7 is only supported version::

    ./locWifi.py

Troubleshooting
===============
First of all, be sure ``geoclue-test-gui`` works.
If it doesn't, then there's likely an issue with DBUS or your WiFi systems.

---
Skyhook update rate is about once per minute--you'll get cached results if you query Skyhook at less than once per minute.

---

> dbus.exceptions.DBusException: org.freedesktop.Geoclue.Error.notAvailable: Geoclue master client has no usable Address providers

This happens if you don't have a working provider configured, or if there isn't an internet connection.


Contributions
=============

The resurrection of this program currently requires Python 2.7 and the deprecated `dbus-python` package.
We'd welcome pull requests building to Python 3 compatibility.
The place to start would be with a Python 3 compatibile Python DBUS API.

Notes
=====

* `Geoclue Reference Manual <https://www.freedesktop.org/software/geoclue/docs/>`_
