from geopy import Nominatim
from .containers import *
import googlemaps
from googlemaps.places import places_nearby


def default_locator_gen():
    agent = 'myGeocoder'
    return Nominatim(user_agent=agent)


'''def __locate(addr: Addr, locator):
    x = __stringify_addr(addr)
    locator.geocode()


def __stringify_addr(addr):
    pass'''


def __parse_gmap(pub: dict) -> Addr:
    x: str = pub['vicinity']
    a = Addr()
    a.house = pub['name']
    y = x.split(sep=', ')
    if len(y) >= 1:
        a.line1 = y[0]
        if len(y) >= 2:
            a.line2 = y[1]
    a.postcode = None

    return a  # gmaps api doesn't return a postcode as global - not worth the extra hassle for the use case


def __default_lookup(coord: Coordinate, dest) -> Optional[Addr]:
    """
    The default implementation that looks up the nearest destination.
    This queries the Google Maps API with the provided destination string
    It then takes the head of any results returned and returns that

    :param coord: the coordinates of the average location
    :param dest: the destination to find near the location
    :return: address of the closest location
    """
    gmaps = __gen_gmap()
    x = coord.latitude, coord.longitude
    # default_radius = 5000  # 5km radius
    nearby = places_nearby(
        client=gmaps,
        location=x,
        # radius=default_radius,
        keyword=dest,
        rank_by='distance',
        open_now=True)
    if nearby is not None and len(nearby['results']) > 0:  # if we find a local destination
        a = __parse_gmap(nearby['results'][0])
        return a
    else:
        return None


def __get_google_key():
    import json
    import os
    fname = 'locationservices/keys.json'
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
