import requests
import requests_cache


class SpinitronSession(requests.Session):
    def __init__(self, api_key: str) -> None:
        super().__init__()
        headers = {'Authorization': 'Bearer ' + api_key}
        self.headers.update(headers)


class CachedSpinitronSession(requests_cache.CachedSession):
    def __init__(self, api_key: str, **kwargs) -> None:
        super().__init__(**kwargs)
        headers = {'Authorization': 'Bearer ' + api_key}
        self.headers.update(headers)