from posixpath import join
from .endpoint import Endpoint
from . import models
from .config import Config
from typing import Mapping

class Spinitron(object):
    host = "http://spinitron.com"
    path = "api"

    def __init__(self, api_key: str, config: Mapping = Config()) -> None:
        config: Config = Config._make(config)

        self.session = config.session(api_key)
        self.spins = Endpoint(self, config.factory(self, models.Spin), "spins")
        self.playlists = Endpoint(self, config.factory(self, models.Playlist), "playlists")
        self.personas = Endpoint(self, config.factory(self, models.Persona), "personas")
        self.shows = Endpoint(self, config.factory(self, models.Show), "shows")

    @property
    def url(self) -> str:
        return join(self.host, self.path)

    def get(self, path: tuple, params: dict) -> dict:
        url = join(self.url, *path)
        response = self.session.get(url, params=params)
        return response.json()
