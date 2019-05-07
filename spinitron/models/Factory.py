from .Listing import Listing

class Factory(object):
    def __init__(self, client, model) -> None:
        super().__init__()
        self.client = client
        self.model = model

    def __call__(self, data):
        if "items" in data:
            items=[]
            for item in data["items"]:
                items.append(self.model(self.client, item))
            data["items"] = items
            return Listing(self.client, data)
        return self.model(self.client, data)