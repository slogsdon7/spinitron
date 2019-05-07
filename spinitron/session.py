import requests
#import requests_cache

#requests_cache.install_cache(expire_after=300)


class SpinitronSession(requests.Session):
    def __init__(self, api_key: str) -> None:
        super().__init__()
        headers = {'Authorization': 'Bearer ' + api_key}
        self.headers.update(headers)
