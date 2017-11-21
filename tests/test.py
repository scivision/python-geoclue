#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2009 - Paulo Cabido <paulo.cabido@gmail.com>
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
from datetime import datetime
import Geoclue as geoclue


# feel free to define your own, it's just .ini style files.
geoloc = geoclue.DiscoverLocation('/usr/share/geoclue-providers')

def test_geolocation():
    geoloc.init()

    loc = geoloc.get_location_info()
    if not loc:
        raise RuntimeError("Could not find location. You may need to run as root.")

    lat = float(loc['latitude'])
    lon = float(loc['longitude'])
    tpos = datetime.fromtimestamp(int(loc['position_timestamp']))

    print("{}: timestamp / Lat / Lon  {}   {} {}".format(
            geoloc.get_position_provider(),tpos,lat,lon))

def location_change():
    print("Location info changed:")
    print(geoloc.get_location_info())


def test_providers():
    geoloc.init()

    providers = geoloc.get_available_providers()
    print('Providers:')
    #print(providers)
    print('\n'.join([p['name'] for p in providers]))
    print('')

    current_position_provider = geoloc.get_position_provider()
    print("Current position provider: {}".format(current_position_provider))


def test_gpsd():
    """
    when a GPS is available, this will pass to the GPS provider
    this will change the master's default provider acording to the requirements
    """

    geoloc.set_requirements(6, 0, True, (1 << 2))

    """
    this will get the current position via GPS but it will continue to use
    the default master provider
    """

    geoloc.set_position_provider("Gpsd")
    """as you can see, the signal function displays the GPS position :-)"""


def test_manual():
    address = {}
    address['street'] = "Rua portuguesa num da porta"
    address['area'] = "Centro Historico"
    address['locality'] = "Evora"
    address['region'] = "Evora"
    address['country'] = "Portugal"
    address['countrycode'] = "PT"
    # Localnet provider also uses the address
    geoloc.set_address_provider("Manual", address)

    current_address_provider = geoloc.get_address_provider()
    print("Current address provider: {}".format(current_address_provider))


#
#print "Reverse address for coordinates lat: 38.5833333 and lon: -7.8333333"
#revgeocoder = geoloc.reverse_position(38.5833333, -7.833333, 3)
#print revgeocoder
#print "\n"
#
## Compare the current position to a given position with a proximity factor of 500m
## It will return true or false
##print "Compare a position to the current position:"
##print "Position to compare, lat: %s lon: %s"
##geoloc.compare_position(LAT, LON, 0.5)

if __name__ == '__main__':
 #   test_providers()
    test_geolocation()