from libAlexa.Core.ResponseBase import ResponseBase
from libAlexa.Core.Interfaces import Interfaces


class Channel(ResponseBase):
    def __init__(self):
        super().__init__()

    def set_channel(self, number, callsign):
        value = {
            "number": number,
            "callSign": callsign,
            "affiliateCallSign": callsign
        }
        super().add_property(Interfaces.ChannelController.value, "channel", value)
