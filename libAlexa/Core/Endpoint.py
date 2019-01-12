class Endpoint:
    def __init__(self, endpointId, friendlyName, manufacturerName, description):
        self.displayCategories = []
        self.cookie = {}
        self.capabilities = []

        self.endpointId = endpointId
        self.friendlyName = friendlyName
        self.manufacturerName = manufacturerName
        self.description = description

    def add_displayCategories(self, category):
        self.displayCategories.append(category)

    def add_cookie(self, cookie):
        cnt = len(self.cookie)
        cnt = cnt + 1
        name = "extraDetail" + str(cnt)
        self.cookie[name] = cookie

    def add_capability(self, capability):
        self.capabilities.append(capability)

    def get_endpoint(self):
        if len(self.displayCategories) <= 0:
            raise ValueError('Display category is mandatory')
        if len(self.cookie) <= 0:
            raise ValueError('Cookie is mandatory')
        if len(self.capabilities) <= 0:
            raise ValueError('Capabilities are mandatory')
        endpoint = {
            "endpointId": self.endpointId,
            "manufacturerName": self.manufacturerName,
            "friendlyName": self.friendlyName,
            "description": self.description,
            "displayCategories": self.displayCategories,
            "cookie": self.cookie,
            "capabilities": self.capabilities
        }
        return endpoint
