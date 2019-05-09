from __future__ import annotations


class Base(object):

    def __init__(self, spinitron, _data) -> None:
        super().__init__()
        self.spinitron = spinitron
        if _data is not None:
            for attribute, value in _data.items():
                setattr(self, attribute, value)
