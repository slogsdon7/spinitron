from .session import SpinitronSession
from posixpath import join
from .endpoint import Endpoint

class Spinitron(object):
    host = "http://spinitron.com"
    path = "api"

    def __init__(self, api_key: str, session=None) -> None:
        if session is None:
            self.session = SpinitronSession(api_key)
        else:
            self.session = session(api_key)

        self.spins = Endpoint(self, None, "spins")
        self.playlists = Endpoint(self, None, "playlists")
        self.personas = Endpoint(self, None, "personas")
        self.shows = Endpoint(self, None, "shows")



    @property
    def url(self) -> str:
        return join(self.host, self.path)

    def get(self, path: tuple, params: dict):
        url = join(self.url, *path)
        response = self.session.get(url, params=params)
        return response.json()



