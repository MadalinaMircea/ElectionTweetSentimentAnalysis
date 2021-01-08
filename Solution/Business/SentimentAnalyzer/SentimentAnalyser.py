from nltk.sentiment.vader import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')


class SentimentAnalyser:
    def __init__(self):
        self.sid = SentimentIntensityAnalyzer()

    def get_tweet_scores(self, text):
        return self.sid.polarity_scores(text)

    def get_all_tweets_scores(self, text_list):
        result = []
        for t in text_list:
            result.append(self.get_tweet_scores(t))
        return result
