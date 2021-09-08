from geopy import Nominatim
from .containers import *
import googlemaps
from googlemaps.places import places_nearby


def default_locator_gen():
    agent = 'myGeocoder'
    return Nominatim(user_agent=agent)


def __locate(addr: Addr, locator):
    x = __stringify_addr(addr)
    locator.geocode()


def __stringify_addr(addr):
    pass


def __default_lookup(coord: Coordinate, dest) -> Addr:
    gmaps = __gen_gmap()
    print('before query')
    x = coord.latitude, coord.longitude
    print(x)
    # default_radius = 5000  # 5km radius
    nearby = places_nearby(
        client=gmaps,
        location=x,
        # radius=default_radius,
        keyword=dest,
        rank_by='distance',
        open_now=True)
    print('after query')
    print(nearby)
    if nearby is not None and nearby['status'] == 200 and len(nearby['results']) > 0:
        return nearby['results'][0]
    else:
        return None


def __get_google_key():
    import json
    import os
    fname = 'locationservices/keys.json'
    print(os.path.exists(fname))
    with open(fname) as f:
        ks = json.load(f)
    if ks is not None:
        return ks['google_key']['key']
    else:
        return None


def __gen_gmap() -> googlemaps.Client:
    default_key = __get_google_key()
    return googlemaps.Client(key=default_key)


def get_nearby(coord: Coordinate, nearby_dest="Wetherspoons",
               lookup_nearby=__default_lookup) -> Addr:
    """
    Returns the closest result from a search on the provided geolocator with the provided phrase

    :param addr: the address to search from - in the default program this is the average address
    :param nearby_dest: the keyword to search for - this finds the nearest Wetherspoons by default
    :param lookup_nearby: the geolocator service to look for the nearest keyword in - by default this is google maps
    Please note that as per the documentation, you will have to provide your own key for the gmaps API
    :return: the address of the nearest keyword (by default the nearest Wetherspoons)
    """
    return lookup_nearby(coord, nearby_dest)


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
