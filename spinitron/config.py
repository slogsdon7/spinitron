from . import models, session, client
from typing import NamedTuple, Callable, Any, Type
import requests


class Config(NamedTuple):
    api_key: str = ""
    url: str = "http://spinitron.com"
    base_path: str = "api"
    session: Type[requests.Session] = session.SpinitronSession
    factory: Callable[[dict], Any] = models.Factory

