from .Base import Base
from .Listing import Listing
from dataclasses import dataclass
from typing import Optional


@dataclass(init=False)
class Persona(Base):
    id: Optional[int] = None
    name: Optional[str] = None
    bio: Optional[str] = None
    since: Optional[int] = None
    email: Optional[str] = None
    website: Optional[str] = None
    image: Optional[str] = None

    def playlists(self, **kwargs) -> Listing:
        params = kwargs
        params["persona_id"] = self.id
        return self.spinitron.playlists(params=params)
