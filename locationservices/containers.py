"""
created to avoid circular imports
this file should call no other in this module
"""
from typing import Optional


class Addr:
    house: str
    line1: str
    line2: Optional[str]
    postcode: Optional[str]

    def __str__(self):
        x = "%s\n%s" % (self.house, self.line1)
        if self.line2 is not None:
            x += "\n%s" % self.line2
        if self.postcode is not None:
            x += "\n%s" % self.postcode
        return x


class Coordinate:
    latitude: float
    longitude: float
