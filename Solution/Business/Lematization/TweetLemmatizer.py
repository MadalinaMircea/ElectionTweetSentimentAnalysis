from nltk.stem import WordNetLemmatizer


class TweetLemmatizerUnit:
    def __init__(self, ontology_labeler):
        self.__lemmatizer = WordNetLemmatizer()
        self.__ontology_labeler = ontology_labeler

    def lemmatize(self, token, use_ontology):
        if use_ontology:
            return self.__ontology_labeler.label(self.__lemmatizer.lemmatize(token))
        else:
            return self.__lemmatizer.lemmatize(token)
