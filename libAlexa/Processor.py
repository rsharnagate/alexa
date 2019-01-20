from libAlexa.Core.Interfaces import Interfaces

class Processor():
    def __init__(self):
        self.isDiscovery = False
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
        self.isDiscovery = namespace == Interfaces.Discovery.value
        messageId = header['messageId']
        payload = request['directive']['payload']

        processed_request = {
            'namespace': namespace,
            'payload': payload,
            'messageId': messageId
        }

        if not self.isDiscovery:
            processed_request['correlationToken'] = header['correlationToken']
            endpoint = request['directive']['endpoint']
            processed_request['endpointId'] = endpoint['endpointId']

            scope = endpoint['scope']
            processed_request['scope_type'] = scope['type']
            processed_request['scope_token'] = scope['token']

        return processed_request
