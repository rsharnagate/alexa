from libAlexa.Processor import Processor
from libAlexa.Core.HttpClient import HttpClient
import json


httpClient = HttpClient()

request = "{\"directive\": {\"header\": {\"namespace\": \"Alexa.Speaker\",\"name\": \"AdjustVolume\",\"messageId\": \"abc-123-def-456\",\"correlationToken\": \"dFMb0z+PgpgdDmluhJ1LddFvSqZ\/jCc8ptlAKulUj90jSqg==\",\"payloadVersion\": \"3\"},\"endpoint\": {\"scope\": {\"type\": \"BearerToken\",\"token\": \"access-token-from-skill\"},\"endpointId\": \"device-001\",\"cookie\": {}},\"payload\": {\"volume\": -20,\"volumeDefault\": false}}}"

processor = Processor()
processed_request = processor.process_request(json.loads(request))

print(processed_request['messageId'])
print(processed_request['namespace'])
print(processed_request['payload'])

if not processor.isDiscovery:
    print(processed_request['endpointId'])
    print(processed_request['correlationToken'])
    print(processed_request['scope_type'])
    print(processed_request['scope_token'])

