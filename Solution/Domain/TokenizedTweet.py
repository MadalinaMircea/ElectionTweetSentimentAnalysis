class TokenizedTweet:
    def __init__(self, id, tokens, text):
        self.__tokens = tokens
        self.__id = id
        self.__text = text

    def get_id(self):
        return self.__id

    @property
    def serialize(self):
        return {"id": self.__id, "tokens": self.__tokens, "text": self.__text}

    def __hash__(self):
        return int(self.__id)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.__id == other.get_id()

    def get_tokens(self):
        return self.__tokens

    def set_tokens(self, tokens):
        self.__tokens = tokens
