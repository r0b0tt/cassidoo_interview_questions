"""
URL Shortener

THis script allows you to shorten and restore urls
"""
import uuid
from typing import Union


class UrlShortener:
    """
    Class to represent the url shortener
    """

    def __init__(self) -> None:
        self.urls = {}

    def shorten(self, url: str) -> str:
        """
        Shortens the ur4()
        """
        for short, value in self.urls.items():
            if value == url:
                return short

        new_short_url = str(uuid.uuid4())[:6]
        self.urls[new_short_url] = url
        return new_short_url

    def restore(self, short: str) -> Union(str, None):
        """
        Restores the url
        """
        stored_url = self.urls.get(short)
        return stored_url


shortener = UrlShortener()
short_url = shortener.shorten("https://google.com")
duplicate_short_url = shortener.shorten("https://google.com")

url = shortener.restore(short_url)
nonexistant_url = shortener.restore("123456")

print(
    f"short_url: {short_url}\nduplicate_short_url: {duplicate_short_url}\nurl={url}\nnonexistant_url={nonexistant_url}"
)
