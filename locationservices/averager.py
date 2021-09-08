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
    :return: container Coordinate containing average latitude and longitude as the crow flies
    """

    locator = generate_locator()
    f = lambda loc: __loc_to_coords(loc, locator)
    coords = map(f, locs)
    n = len(locs)
    latacc, longacc = 0, 0
    print(locs)

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
    place = f"""
    {loc.house},
    {loc.line1},
    {loc.line2},
    {loc.postcode}
    """
    return ltr.geocode(place)
