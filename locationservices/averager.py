from .locator import default_locator_gen
from .containers import *
import time


def average_locations(locs: [Addr],
                      generate_locator=default_locator_gen,
                      delay_s=1) -> Coordinate:
    """
    Takes in a number of addresses; returns the average of the address coordinates

    :param locs: a list containing all addresses to be averaged
    :param generate_locator: the locator to be used - specified from geopy by the calling module. Default is Nominatim
    :param delay_s: the delay between queries to the API. Default is 1 second
    :return:
    """
    locator = generate_locator()
    coords = map(lambda loc: __loc_to_coords(loc, locator), locs)
    n = len(locs)
    latacc, longacc = 0, 0

    for coord in coords:
        latacc += coord.latitude
        longacc += coord.longitude
        time.sleep(delay_s)

    if n > 0:
        l = Coordinate()
        l.latitude = latacc/n
        l.longitude = longacc/n
        return l
    else:
        return None


def __loc_to_coords(loc: Addr, ltr):
    return ltr.geocode(loc)
