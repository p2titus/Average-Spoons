from locator import default_locator_gen
from geopy import Location, Nominatim
import time

Coordinate = (float, float)  # lat, long


class Address:
    house: str
    line1: str
    line2: str
    postcode: str


Addr = Address  # shorthand


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
        return latacc/n, longacc/n
    else:
        return None


def __loc_to_coords(loc: Location, ltr):
    return ltr.geocode(loc)
