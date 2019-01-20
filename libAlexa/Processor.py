from libAlexa.Core.Interfaces import Interfaces


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
        isDiscovery = namespace == Interfaces.Discovery.value
        payload = request['directive']['payload']

        if isDiscovery:
            return None, namespace, payload
        else:
            endpoint = request['directive']['endpoint']
            endpointId = endpoint['endpointId']
            return endpointId, namespace, payload
