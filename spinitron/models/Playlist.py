from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from dataclasses import dataclass
from .Base import Base

if TYPE_CHECKING:
    from .Persona import Persona
    from .Show import Show
    from .Listing import Listing


@dataclass(init=False)
class Playlist(Base):
    id: Optional[int] = None
    persona_id: Optional[int] = None
    show_id: Optional[int] = None
    start: Optional[str] = None
    end: Optional[str] = None
    duration: Optional[int] = None
    timezone: Optional[str] = None
    category: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    since: Optional[int] = None
    url: Optional[str] = None
    hide_dj: Optional[bool] = None
    image: Optional[str] = None
    automation: Optional[bool] = None
    episode_name: Optional[str] = None
    episode_description: Optional[str] = None

    def spins(self, **kwargs) -> Listing:
        params = kwargs
        params['playlist_id'] = self.id
        return self.spinitron.spins(**params)

    def persona(self, **kwargs) -> Persona:
        return self.spinitron.personas(params=kwargs, id=self.persona_id)

    def show(self, **kwargs) -> Show:
        return self.spinitron.shows(params=kwargs, id=self.persona_id)





