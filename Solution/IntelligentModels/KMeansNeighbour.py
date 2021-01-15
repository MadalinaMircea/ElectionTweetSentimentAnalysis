from sklearn.cluster import KMeans
import numpy as np
from joblib import dump, load
import matplotlib.pyplot as plt


class KMeansNeighbour:
    def __init__(self, clusters, random_state, file_path, create=True):
        self.__tokenized_tweets = None
        self.__clusters = clusters
        self.__random_state = random_state
        self.__model = None
        self.__labels = None
        self.__file_path = file_path

        self.LABEL_COLOR_MAP = {0: 'k',
                           1: 'r', 2: 'b', 3: 'y', 4: 'g'
        }

        if create:
            self.create_model()
        else:
            self.load_model()

    def create_model(self):
        self.__model = KMeans(n_clusters=self.__clusters, random_state=self.__random_state)

    def train(self, tokenized_tweets):
        self.__tokenized_tweets = tokenized_tweets
        self.__labels = self.__model.fit_predict(self.__tokenized_tweets)
        dump(self.__model, self.__file_path)

    def load_model(self):
        self.__model = load(self.__file_path)

    def plot_clusters(self, tweets):
        label_color = [self.LABEL_COLOR_MAP[l] for l in self.__labels]
        plt.scatter(tweets[:, 0], tweets[:, 1], c=label_color,
                    s=50, cmap='viridis')

        plt.show()

    def get_cluster(self, tokenized_tweet):
        return self.__model.predict(np.array([np.array(tokenized_tweet)]))[0]
