from typing import Union, Optional, Dict

T_ID = Union[str, int]
T_PARAMS = Dict[str, str]


class Endpoint(object):

    def __init__(self, client, factory, path: str) -> None:
        self.path = path
        self.client = client
        self.factory = factory

    def __call__(self, id: Optional[T_ID] = None, params:Optional[T_PARAMS] = None):
        path = (self.path, str(id)) if id is not None else (self.path,)
        response = self.client.get(path, params)
        return self.factory(response)
