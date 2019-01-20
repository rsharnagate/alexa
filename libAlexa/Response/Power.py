from libAlexa.Core.ResponseBase import ResponseBase
from libAlexa.Core.Interfaces import Interfaces


class Power(ResponseBase):
    def __init__(self):
        super().__init__()

    def set_power(self, value):
        if value is 'ON' or 'OFF':
            super().add_property(Interfaces.PowerController.value, "powerState", str(value).upper())
        else:
            raise ValueError('Expected OFF or ON')
