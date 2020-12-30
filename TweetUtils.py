import re
import twitter


class TweetUtils:
    def __init__(self):
        consumer_key = "NUvnXld1pc6D94DHbmyH7dYIT"
        consumer_secret = "KEsrEHRKLgBkaYtC5x74IsxsGletm87oWm0BGJeOAXmS2l9qMW"
        access_token = "2732573328-Eyo21C9tt7htcbLQqAbnmfcjCO6g3T0KGxJL8l5"
        access_token_secret = "iHVkByWKxGCaxqXTrCnNgSZcheYtL6b3gsf0sc7eWBJiG"

        self.api = twitter.api.Api(consumer_key=consumer_key,
                              consumer_secret=consumer_secret,
                              access_token_key=access_token,
                              access_token_secret=access_token_secret)

    def clean_tweet(self, text):
        text = re.sub("RT ", "", text)
        text = re.sub("@", "", text)
        text = re.sub("https?://[A-Za-z0-9./]*", "", text)
        text = re.sub("\n", "", text)
        return text

    def clean_api_tweet(self, tweets):
        result = []
        for t in tweets:
            result.append(self.clean_tweet(t.text))
        return result

    def get_clean_tweets(self, id_list):
        return self.clean_api_tweet(self.api.GetStatuses(id_list))
