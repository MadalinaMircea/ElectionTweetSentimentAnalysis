from nltk.tokenize import TweetTokenizer
import re
from nltk.corpus import stopwords

from Solution.APIs.TweetUtils import TweetUtils
from Solution.Domain.TokenizedTweet import TokenizedTweet


class TweetTokenizerUnit:
    def __init__(self, lemmatizer):
        self.__tokenizer = TweetTokenizer()
        self.__lemmatizer = lemmatizer
        self.__stopwords = set(stopwords.words('english'))
        self.__tweet_utils = TweetUtils()

    def tokenize(self, tweet, use_ontology):
        text = tweet["text"]
        text = text.lower()
        text = self.__remove_punctuation(text)
        text = self.__remove_numerical(text)
        tokens = self.__tokenizer.tokenize(text)
        tokens = [self.__lemmatizer.lemmatize(token, use_ontology) for token in tokens if token not in self.__stopwords]
        return TokenizedTweet(tweet["id"], tokens, text)

    def __remove_punctuation(self, text):
        return re.sub(r'[^\w\s]', '', text)

    def __remove_numerical(self, text):
        return re.sub(r'[0-9]+', '', text)
