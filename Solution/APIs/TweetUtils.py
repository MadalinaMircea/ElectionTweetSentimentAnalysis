import twitter
import os
import json
from Solution.Domain.Tweet import Tweet
import preprocessor as p
from langdetect import detect
import Solution.config as config


class TweetUtils:
    def __init__(self):
        self.api = twitter.api.Api(consumer_key=config.twitter_keys["consumer_key"],
                                   consumer_secret=config.twitter_keys["consumer_secret"],
                                   access_token_key=config.twitter_keys["access_token"],
                                   access_token_secret=config.twitter_keys["access_token_secret"],
                                   tweet_mode="extended")

        p.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.RESERVED, p.OPT.SMILEY, p.OPT.NUMBER)

    def clean_tweet(self, text):
        # text = re.sub("RT ", "", text)
        # text = re.sub("@", "", text)
        # text = re.sub("https?.* ", " ", text)
        # text = re.sub("https?.*$", "", text)
        # text = re.sub("\n", "", text)
        return p.clean(text)

    def clean_api_tweet(self, tweets):
        result = []
        for t in tweets:
            try:
                if t.full_text != "" and detect(t.full_text) == "en" and t.full_text[:2] != "RT":
                    tweet = Tweet(t.id, self.clean_tweet(t.full_text)).serialize
                    result.append(tweet)
            except:
                pass
        return result

    def add_list_to_set(self, l, s):
        for e in l:
            s.add(e)
        return s

    def get_clean_tweets(self, id_list):
        clean_tweets = []
        k = 0
        if len(id_list) > 4000:
            while len(clean_tweets) < 500:
                print(len(clean_tweets))
                tweets = self.api.GetStatuses(id_list[k:k + 2000])
                k += 2001
                clean_tweets += self.clean_api_tweet(tweets)
        else:
            tweets = self.api.GetStatuses(id_list)
            print(tweets)
            clean_tweets = self.clean_api_tweet(tweets)
            print(clean_tweets)

        return clean_tweets[:500]

    def get_tweets_for_date(self, folder, date, output_file_path):
        print(date)
        if not os.path.exists(output_file_path):
            output_json = {"tweets": []}
        else:
            output_file_read = open(output_file_path, "r+")
            output_json = json.loads(output_file_read.read())
            output_file_read.close()

        output_file_write = open(output_file_path, "w+")

        for month_folder in os.listdir(folder):
            month_path = os.path.join(folder, month_folder)
            for file in os.listdir(month_path):
                if str(date) in file:
                    file_path = os.path.join(month_path, file)
                    file_handle = open(file_path, "r")
                    id_list = file_handle.readlines()
                    file_handle.close()
                    tweets = self.get_clean_tweets(id_list)
                    output_json["tweets"] += tweets
        json_str = json.dumps(output_json, indent=2)
        output_file_write.write(json_str)
        output_file_write.close()

    def get_tweets_for_all_dates(self, folder, dates):
        for (date, file) in dates:
            self.get_tweets_for_date(folder, date, file)
