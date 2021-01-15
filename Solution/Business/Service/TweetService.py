from Solution.Business.Tokenization.TweetTokenizer import TokenizedTweet
from Solution.APIs.TweetUtils import TweetUtils
import numpy as np


class TweetService:
    def __init__(self, tweet_tokenizer, converter, tweet_repository, sentiment_analyser, clustering_model):
        self.__tweet_tokenizer = tweet_tokenizer
        self.__tweet_repository = tweet_repository
        self.__clustering_model = clustering_model
        self.__converter = converter
        self.__sentiment_analyser = sentiment_analyser
        self.__training_data = None
        self.__tweet_utils = TweetUtils()

    def generate_training_data(self, tokenize=True, use_ontology=False):
        if self.__training_data is None:
            tweets = self.__tweet_repository.get_all_tweets()
            self.__training_data = []
            if tokenize:
                for tweet in tweets:
                    tweet["text"] = self.__tweet_utils.clean_tweet(tweet["text"]).strip()
                    if tweet["text"] != "":
                        tokenized = self.__tweet_tokenizer.tokenize(tweet, use_ontology)
                        tokenized = self.__converter.get_vec(tokenized)
                        self.__training_data.append(tokenized.serialize)

    def train_clustering_model(self):
        tweets = self.__tweet_repository.get_all_tweets()
        self.__clustering_model.train(np.array([t["tokens"] for t in tweets]))

    def plot_clusters(self):
        self.__clustering_model.plot_clusters()

    def get_training_data(self):
        return self.__training_data

