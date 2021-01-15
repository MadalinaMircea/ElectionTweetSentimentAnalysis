from gensim.models.doc2vec import TaggedDocument, Doc2Vec


class Doc2VecConversion:
    def __init__(self, information):
        self.__training_data = information["training_data"]
        self.__vector_size = information["vector_size"]
        self.__window = information["window"]
        self.__min_count = information["min_count"]
        self.__workers = information["workers"]
        self.__epochs = information["epochs"]
        self.__model_file = information["model_file"]
        self.__model = None

    def train(self):
        print("Training Doc2Vec")
        documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(self.__training_data)]

        self.__model = Doc2Vec(documents, vector_size=self.__vector_size, window=self.__window,
                               min_count=self.__min_count, workers=self.__workers, epochs=self.__epochs)

        self.__model.save(self.__model_file)

    def get_model(self):
        if self.__model is None:
            self.__model = Doc2Vec.load(self.__model_file)

        return self.__model

    def get_vec(self, tokenized):
        tokens = tokenized.get_tokens()
        converted = self.get_model().infer_vector(tokens).tolist()
        tokenized.set_tokens(converted)
        return tokenized
