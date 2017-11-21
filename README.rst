==============
python-geoclue
==============

Uses available sources of geolocation, including GPS, WiFi BSSID (via Mozilla Location Services), with fallback to IP city-level localization.


Acts as a Python API to DBUS `geoclue`.

.. contents::

Build
=======

Prereqs::

    apt install gcc libdbus-1-dev libdbus-glib-1-dev geoclue

You need a location provider. Here we use Skyhook, but you can select another or several others::

    apt install geoclue-skyhook


Install::

    pip install -e .


Contributions
=============

The resurrection of this program currently requires Python 2.7 and the deprecated `dbus-python` package.
We'd welcome pull requests building to Python 3 compatibility.
The place to start would be with a Python 3 compatibile Python DBUS API.
