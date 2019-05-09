from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING
from .Base import Base

if TYPE_CHECKING:
    from .Playlist import Playlist


@dataclass(init=False)
class Spin(Base):
    id: Optional[int] = None
    playlist_id: Optional[int] = None
    start: Optional[str] = None
    end: Optional[str] = None
    duration: Optional[int] = None
    timezone: Optional[str] = None
    image: Optional[str] = None
    classical: Optional[bool] = None
    artist: Optional[str] = None
    composer: Optional[str] = None
    release: Optional[str] = None
    release_custom: Optional[str] = None
    va: Optional[bool] = None
    label: Optional[str] = None
    label_custom: Optional[str] = None
    released: Optional[int] = None
    medium: Optional[str] = None
    genre: Optional[str] = None
    song: Optional[str] = None
    note: Optional[str] = None
    request: Optional[bool] = None
    local: Optional[bool] = None
    new: Optional[bool] = None
    work: Optional[str] = None
    conductor: Optional[str] = None
    performers: Optional[str] = None
    ensemble: Optional[str] = None
    catalog_number: Optional[str] = None
    isrc: Optional[str] = None
    upc: Optional[str] = None
    iswc: Optional[str] = None

    def playlist(self, **kwargs) -> Playlist:
        return self.spinitron.playlists(self.playlist_id, **kwargs)
