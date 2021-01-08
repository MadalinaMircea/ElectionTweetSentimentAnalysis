class TweetOntologyLabeler:
    def __init__(self, ontology):
        self.__ontology = ontology

    def label(self, token):
        return self.__ontology.get_token_entity(token)
