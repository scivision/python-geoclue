#!/usr/bin/env python
"""
get location using Skyhook Wifi < 100 m accuracy in city.
"""
from time import sleep
from datetime import datetime
import Geoclue
import Geoclue.geoclue

def query_pos(geoloc):
# %% MUST set provider or you'll get cached result until PC reboots!
    geoloc.set_position_provider('Skyhook')
# %% read location and print result
    loc = geoloc.get_location_info()
    if not loc:
        raise RuntimeError("Could not find location. Internet connection is required!")

    return loc

def print_loc(loc):
    """prints location in single line"""

    lat = float(loc['latitude'])
    lon = float(loc['longitude'])
    tpos = datetime.fromtimestamp(int(loc['position_timestamp']))

    stat = "{} {} {} {}".format(
        geoloc.get_position_provider(),tpos,lat,lon)

    print(stat)

    return stat

if __name__ == '__main__':
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('logfile',help='logfile to append location to',nargs='?')
    p = p.parse_args()

    logfile = p.logfile

# %% feel free to define your own, it's just .ini style files.
    geoloc = Geoclue.DiscoverLocation('/usr/share/geoclue-providers')
# %% finer accuracy than LOCALITY causes Skyhook Ubuntu-geoip to not work.
    geoloc.init(accuracy=Geoclue.geoclue.ACCURACY_LEVEL_LOCALITY)

    while True:
        loc = query_pos(geoloc)
        stat = print_loc(loc)

        if logfile:
            with open(logfile,'a') as f:
                f.write(stat+'\n')

        sleep(60) # fastest update rate with Skyhook is one minute



