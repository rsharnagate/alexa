from libAlexa.Processor import Processor
import json


request = "{\"directive\": {\"header\": {\"namespace\": \"Alexa.Speaker\",\"name\": \"AdjustVolume\",\"messageId\": \"abc-123-def-456\",\"correlationToken\": \"dFMb0z+PgpgdDmluhJ1LddFvSqZ\/jCc8ptlAKulUj90jSqg==\",\"payloadVersion\": \"3\"},\"endpoint\": {\"scope\": {\"type\": \"BearerToken\",\"token\": \"access-token-from-skill\"},\"endpointId\": \"device-001\",\"cookie\": {}},\"payload\": {\"volume\": -20,\"volumeDefault\": false}}}"

processor = Processor()
endpointId, namespace, payload, security = processor.process_request(json.loads(request))

print(endpointId)
print(namespace)
print(payload)
print(security)

