
# from SentimentAnalyser import SentimentAnalyser
# from TweetUtils import TweetUtils
# from Domain.Date import Date
#
# tu = TweetUtils()
# sa = SentimentAnalyser()
#
# date_file_comb = [(Date(2020, 10, 28), "Tweets/before_train.json"), (Date(2020, 10, 29), "Tweets/before_train.json"),
#              (Date(2020, 10, 30), "Tweets/before_train.json"),
#              (Date(2020, 10, 31), "Tweets/before_use.json"), (Date(2020, 11, 1), "Tweets/before_use.json"),
#              (Date(2020, 11, 2), "Tweets/before_use.json"),
#              (Date(2020, 11, 3), "Tweets/day_of.json"),
#              (Date(2020, 11, 4), "Tweets/after_use.json"), (Date(2020, 11, 5), "Tweets/after_use.json"),
#              (Date(2020, 11, 6), "Tweets/after_use.json"),
#              (Date(2020, 11, 7), "Tweets/after_train.json"), (Date(2020, 11, 8), "Tweets/after_train.json"),
#              (Date(2020, 11, 9), "Tweets/after_train.json")
#              ]
#
# tu.get_tweets_for_all_dates("Tweets To Use", date_file_comb)
# # tu.get_clean_tweets(["1323778062492803072"])

# import json
# import numpy as np
# from sklearn.cluster import KMeans, SpectralClustering
# import matplotlib.pyplot as plt
#
# file = open("Solution/Data/Tweets/before_train_doc2vec.json", "r")
# data = json.loads(file.read())
# file.close()
#
# tweets = np.array(data["tweets"][:2000])
# print(tweets.shape)
#
# kmeans = SpectralClustering(n_clusters=4, affinity='nearest_neighbors', assign_labels='kmeans')
# clusters = kmeans.fit_predict(tweets)
#
# plt.scatter(tweets[:, 0], tweets[:, 1], c=clusters,
#             s=50, cmap='viridis')
#
# plt.show()


from Solution.Business.Conversion.Doc2VecConversion import Doc2VecConversion
from Solution.Business.Ontology.Ontology import Ontology
from Solution.Business.Service.TweetService import TweetService
from Solution.Business.Tokenization.TweetTokenizer import TweetTokenizerUnit
from Solution.Business.Lematization.TweetLemmatizer import TweetLemmatizerUnit
from Solution.Persistency.TweetRepository import TweetRepository
from Solution.IntelligentModels.KMeansNeighbour import KMeansNeighbour
from Solution.Business.SentimentAnalyzer.SentimentAnalyser import SentimentAnalyser
import json
import numpy as np
from random import sample

sentiment_analyser = SentimentAnalyser()
ontology = Ontology("Solution/Data/Ontology/TweetOntology.owl")
lemmatizer = TweetLemmatizerUnit(ontology)
tokenizer = TweetTokenizerUnit(lemmatizer)
repo = TweetRepository("Solution/Data/Tweets/after_use_ontologized_doc2vec.json")
# information = {"training_data": [], "vector_size": 20, "window": 2, "min_count": 1, "workers": 4, "epochs": 100,
#                "model_file": "Solution/test_doc2vec.model"}
# converter = Doc2VecConversion(information)
# service = TweetService(tokenizer, converter, repo, sentiment_analyser, None)
# service.generate_training_data(True, True)

trump = {"pos_tweets": [], "pos": 0, "neg_tweets": [], "neg": 0}
biden = {"pos_tweets": [], "pos": 0, "neg_tweets": [], "neg": 0}

for tweet in repo.get_all_tweets():
    sentiments = sentiment_analyser.get_tweet_scores(tweet["text"])
    is_trump = ("trump" in tweet["text"] or "republican" in tweet["text"])
    is_biden = ("biden" in tweet["text"] or "democrat" in tweet["text"])
    if is_trump and not is_biden:
        if sentiments["pos"] > sentiments["neg"]:
            trump["pos_tweets"].append(tweet)
            trump["pos"] += sentiments["pos"]
        else:
            trump["neg_tweets"].append(tweet)
            trump["neg"] += sentiments["neg"]
    if not is_trump and is_biden:
        if sentiments["pos"] > sentiments["neg"]:
            biden["pos_tweets"].append(tweet)
            biden["pos"] += sentiments["pos"]
        else:
            biden["neg_tweets"].append(tweet)
            biden["neg"] += sentiments["neg"]

print("\nTrump\n")
print("Positive tweets")
for tweet in sample(trump["pos_tweets"], 5):
    print(tweet["text"])
print("Negative tweets")
for tweet in sample(trump["neg_tweets"], 5):
    print(tweet["text"])

print("\nPositive total: " + str(len(trump["pos_tweets"])))
print("Negative total: " + str(len(trump["neg_tweets"])))
print("Positive average: " + str(trump["pos"] / len(trump["pos_tweets"])))
print("Negative average: " + str(trump["neg"] / len(trump["neg_tweets"])))


print("\n\n\nBiden\n")
print("Positive tweets")
for tweet in sample(biden["pos_tweets"], 5):
    print(tweet["text"])
print("Negative tweets")
for tweet in sample(biden["neg_tweets"], 5):
    print(tweet["text"])

print("\nPositive total: " + str(len(biden["pos_tweets"])))
print("Negative total: " + str(len(biden["neg_tweets"])))
print("Positive average: " + str(biden["pos"] / len(biden["pos_tweets"])))
print("Negative average: " + str(biden["neg"] / len(biden["neg_tweets"])))

# trump = []
#
# clustering = KMeansNeighbour(2, 0, 'kmeans_model_all_after_rk.joblib', True)
#
# for tweet in repo.get_all_tweets():
#     sentiments = sentiment_analyser.get_tweet_scores(tweet["text"])
#     sent_list = [sentiments["pos"], sentiments["neg"], 0, 0]
#     if "trump" in tweet["text"]:
#         sent_list[2] = 1
#     if "biden" in tweet["text"]:
#         sent_list[3] = 1
#     trump.append(sent_list)
#
# trump = np.array(trump)
# clustering.train(trump)
#
# clusters = {0: {"pos": 0, "neg": 0, "total": 0}, 1: {"pos": 0, "neg": 0, "total": 0}}
#
# for t in trump:
#     # sentiments = sentiment_analyser.get_tweet_scores(tweet["text"])
#     # sent_list = [sentiments["pos"], sentiments["neg"]]
#     cluster = clustering.get_cluster(np.array(t))
#     clusters[cluster]["pos"] += t[0]
#     clusters[cluster]["neg"] += t[1]
#     clusters[cluster]["total"] += 1
#
# for c in clusters:
#     print(c)
#     print("Positive: " + str(clusters[c]["pos"] / clusters[c]["total"]))
#     print("Negative: " + str(clusters[c]["neg"] / clusters[c]["total"]))
#     print("Total: " + str(clusters[c]["total"]))
#     print()
#
# clustering.plot_clusters(trump)


# clustering.train(np.array(trump))
# clustering.plot_clusters(np.array(biden))

# clustering = KMeansNeighbour(2, 0, 'kmeans_model_biden_only_sentiments_3.joblib', True)
# clustering.train(np.array(biden))
# clustering.plot_clusters()

#
# service.train_clustering_model()
# service.plot_clusters()

# service.generate_training_data(True, True)
#
# result = {"tweets": service.get_training_data()}
# file = open("Solution/Data/Tweets/after_use_ontologized_doc2vec.json", "w+")
# file.write(json.dumps(result, indent=2))
# file.close()

