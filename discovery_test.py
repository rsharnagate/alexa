from libAlexa.Processor import Processor
import json

discovery_request = "{\"directive\":{\"header\":{\"namespace\":\"Alexa.Discovery\",\"name\": \"Discover\",\"payloadVersion\": \"3\",\"messageId\":\"abc-123-def-456\"},\"payload\":{\"scope\": {\"type\": \"BearerToken\",\"token\": \"access-token-from-skill\"}}}}"

processor = Processor()
endpointId, namespace, payload = processor.process_request(json.loads(discovery_request))

print(endpointId)
print(namespace)
print(payload)
