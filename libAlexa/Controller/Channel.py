from libAlexa.Core.CapabilityBase import CapabilityBase
from libAlexa.Core.Interfaces import Interfaces
from libAlexa.Core.Properties import Properties


class Channel(CapabilityBase):
    def __init__(self):
        properties = Properties(True, True)
        properties.add_support("channel")
        super().__init__(Interfaces.ChannelController.value, properties.get_properties())
