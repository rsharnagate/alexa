from libAlexa.Core.CapatibilityBase import CapabilityBase
from libAlexa.Core.Interfaces import Interfaces
from libAlexa.Core.Properties import Properties


class Speaker(CapabilityBase):
    def __init__(self):
        properties = Properties(True, True)
        properties.add_support("volume")
        properties.add_support("muted")
        super().__init__(Interfaces.Speaker.value, properties.get_properties())
