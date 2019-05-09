from . import models, session
from typing import NamedTuple, Callable, Any
import os


class Config(NamedTuple):
    api_key: str = os.environ.get("SPINITRON_KEY")
    cached_session = session.CachedSpinitronSession
    session = session.SpinitronSession
    factory: Callable[[dict], Any] = models.Factory

