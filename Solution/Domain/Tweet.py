class Tweet:
    def __init__(self, id, text):
        self.id = id
        self.text = text

    @property
    def serialize(self):
        return {"id": self.id, "text": self.text}

    def __hash__(self):
        return int(self.id)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id
