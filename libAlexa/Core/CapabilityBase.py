from libAlexa.Core import Constant


class CapabilityBase:
    def __init__(self, interface, properties=None):
        self.interface = interface
        self.properties = properties

    def get_capability(self):
        capability = {
            "type": Constant.CAPABILITY_TYPE,
            "interface": self.interface,
            "version": Constant.API_VERSION
        }
        if self.properties is not None:
            capability["properties"] = self.properties

        return capability
