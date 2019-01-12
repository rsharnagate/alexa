class Properties:
    def __init__(self, proactivelyReported, retrievable):
        self.support = []
        self.proactivelyReported = proactivelyReported
        self.retrievable = retrievable

    def add_support(self, support):
        self.support.append({"name": support})

    def get_properties(self):
        properties = {
            "supported": self.support,
            "proactivelyReported": self.proactivelyReported,
            "retrievable": self.retrievable
        }
        return properties
