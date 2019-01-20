from libAlexa.Core.CapatibilityBase import CapabilityBase
from libAlexa.Core.Interfaces import Interfaces
from libAlexa.Core.Properties import Properties


class Alexa(CapabilityBase):
    def __init__(self):
        super().__init__(Interfaces.Alexa.value)
