from typing import Union, Optional, Dict

T_ID = Union[str, int]
T_PARAMS = Dict[str, str]

class Endpoint(object):

    def __init__(self, client, model, path: str) -> None:
        self.path = path
        self.client = client
        self.model = model

    def __call__(self, id: Optional[T_ID] = None, params=Optional[T_PARAMS]):
        path = (self.path, id) if id is not None else (self.path,)
        response = self.client.get(path, params)
        return response
