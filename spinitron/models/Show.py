from dataclasses import dataclass
from .Base import Base
from typing import Optional


@dataclass(init=False)
class Show(Base):
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
