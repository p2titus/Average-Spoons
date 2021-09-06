import geopandas
import geopy
from geopy import Location, Nominatim
import time

Coordinate = (float, float)


class Addr:
    house: str
    line1: str
    line2: str
    postcode: str


def __default_locator_gen():
    agent = 'myGeocoder'
    return Nominatim(user_agent=agent)


"""
delay_s is to ensure apis aren't queried too frequently
"""
def average_locations(locs: [Addr],
                      generate_locator=__default_locator_gen,
                      delay_s=1) -> Coordinate:
    locator = generate_locator()
    coords = map(lambda loc: __loc_to_coords(loc, locator), locs)
    n = len(locs)
    latacc, longacc = 0, 0

    for coord in coords:
        latacc += coord.latitude
        longacc += coord.longitude
        time.sleep(delay_s)

    if n > 0:
        return latacc/n, longacc/n
    else:
        return None








def __loc_to_coords(loc: Location, ltr):
    return ltr.geocode(loc)
