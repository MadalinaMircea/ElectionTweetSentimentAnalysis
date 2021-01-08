from sklearn.cluster import KMeans
import numpy as np
from joblib import dump, load


class KMeansNeighbour:
    def __init__(self, tokenized_tweets, clusters, random_state, create=True):
        self.__tokenized_tweets = np.array(tokenized_tweets)
        self.__clusters = clusters
        self.__random_state = random_state
        self.__model = None

        if create:
            self.create_model()
        else:
            self.load_model()

    def create_model(self):
        self.__model = KMeans(n_clusters=self.__clusters, random_state=self.__random_state)

    def train(self):
        self.__model.fit(self.__tokenized_tweets)
        dump(self.__model, 'kmeans_model.joblib')

    def load_model(self):
        self.__model = load('kmeans_model.joblib')

    def get_cluster(self, tokenized_tweet):
        return self.__model.predict(np.array([np.array(tokenized_tweet)]))[0]
