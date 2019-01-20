from libAlexa.Core.ResponseBase import ResponseBase


class Discovery(ResponseBase):
    def __init__(self):
        super().__init__()

    def get_response(self, request, endpoints=None):
        if endpoints is None or len(endpoints) <= 0:
            raise ValueError('No endpoints found')

        header = request['directive']['header']
        messageId = header['messageId']
        response = {
            "event": {
                "header": {
                    "namespace": "Alexa.Discovery",
                    "name": "Discover.Response",
                    "payloadVersion": "3",
                    "messageId": messageId
                },
                "payload": {
                    "endpoints": endpoints
                }
            }
        }
        return response
