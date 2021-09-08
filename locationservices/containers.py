"""
created to avoid circular imports
this file should call no other in this module
"""


class Addr:
    house: str
    line1: str
    line2: str
    postcode: str


class Coordinate:
    latitude: float
    longitude: float
