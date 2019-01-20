from libAlexa.Core.ResponseBase import ResponseBase
from libAlexa.Core.Constant import API_VERSION


class AcceptGrant(ResponseBase):
    def __init__(self):
        super().__init__()

    def get_response(self, request, endpoints=None):
        header = request['directive']['header']
        messageId = header['messageId']
        response = {
            "event": {
                "header": {
                    "namespace": "Alexa.Authorization",
                    "name": "AcceptGrant.Response",
                    "payloadVersion":  API_VERSION,
                    "messageId": messageId
                },
                "payload": {}
            }
        }
        return response
