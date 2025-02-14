from even_location import EvenLocation
import validators


class UrlEventLocation(EvenLocation):
    def __init__(self, url: str):
        if validators.url(url):
            self._url = url
        else:
            raise ValueError(f"url: {url} is not valid")

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value: str):
        if validators.url(value):
            self._url = value
        else:
            raise ValueError(f"url: {value} is not valid")

    def to_str(self):
        return self.url
