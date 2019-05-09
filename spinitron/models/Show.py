from dataclasses import dataclass
from .Base import Base
from .Listing import Listing
from typing import Optional


@dataclass(init=False)
class Show(Base):
    id: Optional[int] = None
    start: Optional[str] = None
    end: Optional[str] = None
    duration: Optional[int] = None
    timezone: Optional[str] = None
    one_off: Optional[bool] = None
    category: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    since: Optional[int] = None
    url: Optional[str] = None
    hide_dj: Optional[bool] = None
    image: Optional[str] = None

    def playlists(self, **kwargs) -> Listing:
        params = kwargs
        params["show_id"] = self.id
        return self.spinitron.playlists(params=params)

    def spins(self, **kwargs) -> Listing:
        params = kwargs
        params["show_id"] = self.id
        return self.spinitron.playlists(params=params)