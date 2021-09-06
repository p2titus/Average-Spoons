import geopandas
import geopy
from geopy import Location, Nominatim
import time

class Addr:
    house: str
    line1: str
    line2: str
    postcode: str
    coords: (float, float)


def __default_locator_gen():
    agent = 'myGeocoder'
    return Nominatim(user_agent=agent)


"""
delay_s is to ensure apis aren't queried too frequently
"""
def average_locations(locs: [Addr],
                      generate_locator=__default_locator_gen,
                      delay_s=1) -> Addr:
    locator = generate_locator()
    coords = map(lambda loc: __loc_to_coords(loc, locator), locs)
    latacc, longacc = 0, 0

    for coord in coords:
        latacc += coord.latitude
        longacc += coord.longitude
        time.sleep(delay_s)








def __loc_to_coords(loc: Location, ltr):
    return ltr.geocode(loc)
