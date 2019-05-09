from __future__ import annotations

from .Listing import Listing
from typing import Union, TypeVar, Callable

T = TypeVar("T")


class Factory(object):
    endpoint: Callable

    def __init__(self, client,  model: T) -> None:
        super().__init__()
        self.client = client
        self.model = model

    def __call__(self, data: dict) -> Union[T, Listing]:
        if "items" in data:
            items=[]
            for item in data["items"]:
                items.append(self.model(self.client, item))
            data["items"] = items
            return Listing(self.client, self.endpoint, data)
        return self.model(self.client, data)

