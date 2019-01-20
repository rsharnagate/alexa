from libAlexa.Processor import Processor
import json

discovery_request = "{\"directive\":{\"header\":{\"namespace\":\"Alexa.Discovery\",\"name\": \"Discover\",\"payloadVersion\": \"3\",\"messageId\":\"abc-123-def-456\"},\"payload\":{\"scope\": {\"type\": \"BearerToken\",\"token\": \"access-token-from-skill\"}}}}"


processor = Processor()
processed_request = processor.process_request(json.loads(discovery_request))

print(processed_request['messageId'])
print(processed_request['namespace'])
print(processed_request['payload'])

if not processor.isDiscovery:
    print(processed_request['endpointId'])
    print(processed_request['correlationToken'])
    print(processed_request['scope_type'])
    print(processed_request['scope_token'])
