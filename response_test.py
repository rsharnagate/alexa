from libAlexa.Response.Power import Power
from libAlexa.Endpoint.Power import Power
from libAlexa.Response.Speaker import Speaker
from libAlexa.Response.Discovery import Discovery
from libAlexa.Core.Endpoint import Endpoint
import json

endpoint = Endpoint("RBS-LIVING-ROOM-TV-01", "TataSky", "TataSky", "TataSky connected TV")
endpoint.add_displayCategories("TV")
endpoint.add_cookie("Livingroom LED TV")
endpoint.add_cookie("connected to TataSky")

power = Power()
endpoint.add_capability(power.get_capability())
request = "{\"directive\":{\"header\":{\"namespace\": \"Alexa.Discovery\",\"name\": \"Discover\",\"payloadVersion\":\"3\",\"messageId\": \"abc-123-def-456\"},\"payload\":{\"scope\":{\"type\": \"BearerToken\",\"token\": \"access-token-from-skill\"}}}}"
discovery = Discovery()
print(discovery.get_response(json.loads(request), [endpoint.get_endpoint()]))

# request = "{\"directive\":{\"header\":{\"namespace\":\"Alexa.Speaker\",\"name\":\"SetVolume\",\"messageId\":\"5f8a426e-01e4-4cc9-8b79-65f8bd0fd8a4\",\"correlationToken\":\"dFMb0z+PgpgdDmluhJ1LddFvSqZ\/jCc8ptlAKulUj90jSqg==\",\"payloadVersion\":\"3\"},\"endpoint\":{\"scope\":{\"type\":\"BearerToken\",\"token\":\"access-token-from-skill\"},\"endpointId\":\"device-001\",\"cookie\":{}},\"payload\":{\"volume\": 50}}}"
# speaker = Speaker()
# speaker.set_muted(False)
# speaker.set_volume(50)
# print(speaker.get_response(json.loads(request)))
#
# request = "{\"directive\":{\"header\":{\"namespace\":\"Alexa.PowerController\",\"name\":\"TurnOn\",\"payloadVersion\":\"3\",\"messageId\":\"1bd5d003-31b9-476f-ad03-71d471922820\",\"correlationToken\":\"dFMb0z+PgpgdDmluhJ1LddFvSqZ\/jCc8ptlAKulUj90jSqg==\"},\"endpoint\":{\"scope\":{\"type\": \"BearerToken\",\"token\":\"access-token-from-skill\"},\"endpointId\":\"appliance-001\",\"cookie\":{}},\"payload\":{}}}"
# power = Power()
# power.set_power('on')
# print(power.get_response(json.loads(request)))