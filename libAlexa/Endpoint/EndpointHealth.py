from libAlexa.Core.CapatibilityBase import CapabilityBase
from libAlexa.Core.Interfaces import Interfaces
from libAlexa.Core.Properties import Properties


class EndpointHealth(CapabilityBase):
    def __init__(self):
        properties = Properties(True, True)
        properties.add_support("connectivity")
        super().__init__(Interfaces.EndpointHealth.value, properties.get_properties())
