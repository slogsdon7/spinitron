from typing import Union, Callable
from .Base import Base


class Listing(Base):
    endpoint: Callable
    items: list
    _meta: dict

    def __init__(self, spinitron, endpoint, _data, **kwargs) -> None:
        super().__init__(spinitron, _data)
        self.endpoint = endpoint
        self.params = kwargs

    @property
    def page_count(self) -> Union[int, bool]:
        return self._meta["pageCount"]

    @property
    def current_page(self) -> int:
        return self._meta["currentPage"]

    @property
    def per_page(self) -> int:
        return self._meta["perPage"]

    @property
    def total_count(self) -> Union[int, bool]:
        return self._meta["totalCount"]

    def __iter__(self):
        yield self
        if self.page_count:
            while self.current_page < self.page_count:
                params = {"count": self.per_page, "page": self.current_page + 1}
                yield self.endpoint(**params)
        else:
            while len(self.items) > 0:
                params = {"count": self.per_page, "page": self.current_page + 1}
                yield self.endpoint(**params)

    def __getitem__(self, index):
        params = self.params
        params['page'] = index
        if not isinstance(index, int):
            raise TypeError
        if self.page_count:
            if self.page_count < index or self.page_count < 0:
                raise IndexError
        else:
            result = self.endpoint(**params)
            if len(result.items) > 0:
                return result
            else:
                raise IndexError
        params['page'] = index
        return self.endpoint(**params)
