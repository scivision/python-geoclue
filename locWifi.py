#!/usr/bin/env python
"""
get location using Skyhook Wifi < 100 m accuracy in city.
"""
from datetime import datetime
import Geoclue
import Geoclue.geoclue


# feel free to define your own, it's just .ini style files.
geoloc = Geoclue.DiscoverLocation('/usr/share/geoclue-providers')

# finer accuracy than LOCALITY causes Skyhook Ubuntu-geoip to not work.
geoloc.init(accuracy=Geoclue.geoclue.ACCURACY_LEVEL_LOCALITY)
#    geoloc.signal()

# %% MUST set provider or you'll get cached result until PC reboots!
geoloc.set_position_provider('Skyhook')
# %% read location and print result
loc = geoloc.get_location_info()
if not loc:
    raise RuntimeError("Could not find location. Internet connection is required!")

lat = float(loc['latitude'])
lon = float(loc['longitude'])
tpos = datetime.fromtimestamp(int(loc['position_timestamp']))

print("{}: timestamp / Lat / Lon  {}   {} {}".format(
        geoloc.get_position_provider(),tpos,lat,lon))

