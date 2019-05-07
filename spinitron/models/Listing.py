from typing import NamedTuple, Union
from .Base import Base

class Pagination(NamedTuple):
    totalCount = Union[int, bool]
    pageCount = Union[int, bool]
    currentPage = int
    perPage = int


class Listing(Base):

    @classmethod
    def factory(cls, client, model, _data):
        if "items" in _data:
            items=[]
            for item in _data["items"]:
                items.append(model(client, item))
            _data["items"] = items
            return cls(client, _data)
        return model(client, _data)


