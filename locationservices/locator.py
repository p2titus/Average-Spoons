from geopy import Nominatim
from averager import Addr, Coordinate
import googlemaps
from googlemaps.places import places_nearby


def default_locator_gen():
    agent = 'myGeocoder'
    return Nominatim(user_agent=agent)


def __default_lookup(coord: Coordinate, dest) -> Addr:
    gmaps = __gen_gmap()
    default_radius = 5000  # 5km radius
    nearby = places_nearby(
        client=gmaps,
        location=coord,
        radius=default_radius,
        keyword=dest,
        rank_by='distance',
        open_now=True)
    if nearby['status'] == 200 and len(nearby['results']) > 0:
        return nearby['results'][0]
    else:
        return None


def __get_google_key():
    import json
    fname = 'keys.json'
    ks = None
    with open(fname) as f:
        ks = json.load(f)
    if ks is not None:
        return ks['google_key']['key']
    else:
        return None


def __gen_gmap() -> googlemaps.Client:
    default_key = __get_google_key()
    return googlemaps.Client(key=default_key)


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
