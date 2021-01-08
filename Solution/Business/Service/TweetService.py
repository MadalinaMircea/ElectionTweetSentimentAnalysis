class TweetService:
    def __init__(self, tweet_tokenizer, tweet_repository, clustering_model):
        self.__tweet_tokenizer = tweet_tokenizer
        self.__tweet_repository = tweet_repository
        self.__clustering_model = clustering_model
        self.__training_data = None

    def generate_training_data(self, tokenize=True, use_ontology=False):
        if self.__training_data is None:
            tweets = self.__tweet_repository.get_all_tweets()
            if tokenize:
                tweets = [self.__tweet_tokenizer.tokenize(tweet, use_ontology) for tweet in tweets]
            self.__training_data = tweets

    def train_clustering_model(self):
        pass

    def get_training_data(self):
        return self.__training_data

