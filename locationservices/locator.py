
from averager import Addr, Coordinate, __default_locator_gen
import googlemaps
from googlemaps import places


def default_locator_gen():
    agent = 'myGeocoder'
    return Nominatim(user_agent=agent)


def __default_lookup(addr: Addr, dest) -> Addr:
    default_key = None  # TODO - get proper key
    gmaps = googlemaps.Client(key=default_key)
    gmaps.places.places_nearby()
    return None


def get_nearby(addr: Addr, nearby_dest="Wetherspoons",
               lookup_nearby=__default_lookup) -> Addr:
    return lookup_nearby(addr, nearby_dest)


def __default_trans(c: Coordinate):
    l = default_locator_gen()
    lat, long = c
    postcode = l.reverse(str(lat), str(long))
    address = Addr()
    address.postcode = postcode
    return address


def translate_coords_addr(coordinate: Coordinate,
                          translator=__default_trans) -> Addr:
    return translator(coordinate)
