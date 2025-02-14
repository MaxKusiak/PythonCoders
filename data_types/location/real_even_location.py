from even_location import EvenLocation


class RealEvenLocation(EvenLocation):
    def __init__(self, location: str):
        self._location = location

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value: str):
        self._location = value

    def to_str(self):
        return self.location
