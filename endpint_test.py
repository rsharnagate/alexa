from libAlexa.Core.Endpoint import Endpoint
from libAlexa.Endpoint.Power import Power
from libAlexa.Endpoint.Speaker import Speaker
from libAlexa.Endpoint.Channel import Channel
from libAlexa.Endpoint.EndpointHealth import EndpointHealth
from libAlexa.Endpoint.Alexa import Alexa

endpoint = Endpoint("RBS-LIVING-ROOM-TV-01", "TataSky", "TataSky", "TataSky connected TV")
endpoint.add_displayCategories("TV")
endpoint.add_cookie("Livingroom LED TV")
endpoint.add_cookie("connected to TataSky")

power = Power()
endpoint.add_capability(power.get_capability())

speaker = Speaker()
endpoint.add_capability(speaker.get_capability())

channel = Channel()
endpoint.add_capability(channel.get_capability())

endpointHealth = EndpointHealth()
endpoint.add_capability(endpointHealth.get_capability())

alexa = Alexa()
endpoint.add_capability(alexa.get_capability())

print(endpoint.get_endpoint())
