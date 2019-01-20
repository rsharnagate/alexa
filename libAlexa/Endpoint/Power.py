from libAlexa.Core.CapatibilityBase import CapabilityBase
from libAlexa.Core.Interfaces import Interfaces
from libAlexa.Core.Properties import Properties


class Power(CapabilityBase):
    def __init__(self):
        properties = Properties(True, True)
        properties.add_support("powerState")
        super().__init__(Interfaces.PowerController.value, properties.get_properties())
