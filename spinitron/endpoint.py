from typing import Union, Optional, Dict

T_ID = Union[str, int]
T_PARAMS = Dict[str, str]


class Endpoint(object):

    def __init__(self, client, factory, path: str) -> None:
        self.path = path
        self.client = client
        self.factory = factory
        self.factory.endpoint = self

    def __call__(self, id: Optional[T_ID] = None, **kwargs: Union[str, int]):
        path = (self.path, str(id)) if id is not None else (self.path,)
        response = self.client.get(path, **kwargs)
        return self.factory(response)
