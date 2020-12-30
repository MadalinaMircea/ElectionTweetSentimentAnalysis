from SentimentAnalyser import SentimentAnalyser
from TweetUtils import TweetUtils

tu = TweetUtils()
sa = SentimentAnalyser()

result = tu.get_clean_tweets(["1311501067679485952", "1311501067801198592"])
print(result)

print(sa.get_all_tweets_scores(result))
