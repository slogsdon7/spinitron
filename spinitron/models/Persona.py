from .Base import Base
from dataclasses import dataclass
from typing import Optional


@dataclass(init=False)
class Persona(Base):
    id: int
    name: Optional[str] = None
    bio: Optional[str] = None
    since: Optional[int] = None
    email: Optional[str] = None
    website: Optional[str] = None
    image: Optional[str] = None
