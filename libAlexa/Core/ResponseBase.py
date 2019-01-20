from libAlexa.Core import Util, Constant


class ResponseBase:
    def __init__(self):
        self.properties = []

    def add_property(self, interface, name, value):
        prop = {
            "namespace": interface,
            "name": name,
            "value": value,
            "timeOfSample": Util.get_utc_timestamp(),
            "uncertaintyInMilliseconds": 0
        }
        self.properties.append(prop)

    def get_response(self, request, endpoints=None):
        if len(self.properties) <= 0:
            raise ValueError('There must be atleast one property defined')

        header = request['directive']['header']
        messageId = header['messageId']
        correlationToken = header['correlationToken']
        endpoint = request['directive']['endpoint']
        endpointId = endpoint['endpointId']
        scope = endpoint['scope']
        scope_type = scope['type']
        scope_token = scope['token']
        response = {
            "context": {
                "properties": self.properties
            },
            "event": {
                "header": {
                    "namespace": "Alexa",
                    "name": "Response",
                    "payloadVersion": Constant.API_VERSION,
                    "messageId": messageId,
                    "correlationToken": correlationToken
                },
                "endpoint": {
                    "scope": {
                        "type": scope_type,
                        "token": scope_token
                    },
                    "endpointId": endpointId
                },
                "payload": {}
            }
        }
        return response
