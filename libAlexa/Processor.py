class Processor():
    def __init__(self):
        pass

    def get_payload_version(self, request):
        try:
            return request["directive"]["header"]["payloadVersion"]
        except:
            try:
                return request["header"]["payloadVersion"]
            except:
                return "-1"

    def process_request(self, request):
        payloadVersion = self.get_payload_version(request)
        if payloadVersion != "3":
            print("Received payload version " + payloadVersion + ", aborting request.")
            return

        header = request['directive']['header']
        namespace = header['namespace']
        messageId = header['messageId']
        correlationToken = header['correlationToken']

        endpoint = request['directive']['endpoint']
        endpointId = endpoint['endpointId']

        scope = endpoint['scope']
        scope_type = scope['type']
        scope_token = scope['token']

        payload = request['directive']['payload']

        security = {
            'messageId': messageId,
            'correlationToken': correlationToken,
            'scope_type': scope_type,
            'scope_token': scope_token
        }

        return endpointId, namespace, payload, security
