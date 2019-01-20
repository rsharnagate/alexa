from libAlexa.Core.ResponseBase import ResponseBase
from libAlexa.Core.Interfaces import Interfaces


class Speaker(ResponseBase):
    def __init__(self):
        super().__init__()

    def set_volume(self, value):
        if type(value) is int:
            super().add_property(Interfaces.Speaker.value, "volume", value)
        else:
            raise ValueError('Expected integer value')

    def set_muted(self, value):
        if type(value) is bool:
            super().add_property(Interfaces.Speaker.value, "muted", value)
        else:
            raise ValueError('Expected boolean value')
