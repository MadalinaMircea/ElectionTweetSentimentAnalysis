from Solution.Tests.Tests import Tests
from Solution.Persistency.TweetRepository import TweetRepository
from Solution.Business.Ontology.TweetOntologyLabeler import TweetOntologyLabeler
from Solution.Business.Ontology.Ontology import Ontology
from Solution.Business.Lematization.TweetLemmatizer import TweetLemmatizerUnit
from Solution.Business.Tokenization.TweetTokenizer import TweetTokenizerUnit
from Solution.Business.Service.TweetService import TweetService
import json


# print("Creating variables...")
# repo = TweetRepository("Data/Tweets/before_train.json")
# ontology = Ontology("Data/Ontology/TweetOntology.owl")
# labeler = TweetOntologyLabeler(ontology)
# lemmatizer = TweetLemmatizerUnit(labeler)
# tokenizer = TweetTokenizerUnit(lemmatizer)
# clustering_model = None
# service = TweetService(tokenizer, repo, clustering_model)

# print("Generating training data...")
# service.generate_training_data(True, True)
# training_data = service.get_training_data()
#
# json_data = []
# for x in training_data:
#     print(x.serialize)
#     json_data.append(x.serialize)
#
# file = open("Data/Tweets/before_train_tokenized_lemmatized_ontologized.json", "w+")
# data_json = json.dumps({"tweets": json_data}, indent=2)
# file.write(data_json)
# file.close()
#
# print("Running tests...")
# tests = Tests()
# tests.run_all_tests()
#
# from Solution.UI.WordCloudCreator import WordCloudCreator
#
# wc = WordCloudCreator({"type": "json_file", "file_path": "../Tweets/before_train_tokenized_lemmatized_combined.txt",
#                       "background_color": "white"})
#
# # wc.plot()
# # wc.save_to_file("lemmatized_all_wordcloud.png")
#
# result = {"words": []}
# for (word, freq) in wc.get_frequencies(200):
#     result["words"].append((word, freq))
#
# import json
# json_str = json.dumps(result, indent=2)
# output_file_write = open("../Tweets/before_train_all_word_frequency.json", "w+")
# output_file_write.write(json_str)
# output_file_write.close()

# from Solution.Business.Conversion.Doc2VecConversion import Doc2VecConversion
#
# information = {"training_data": None, "model_file": "test_doc2vec.model", "vector_size": 20, "window": 2,
#                "min_count": 1, "workers": 4, "epochs": 100}
# dv = Doc2VecConversion(information)
#
# from Solution.IntelligentModels.KMeansNeighbour import KMeansNeighbour
# import json
#
# print("Starting...")
# file = open("../Tweets/before_train_tokenized_lemmatized.txt", "r")
# tweet_json = json.loads(file.read())
# file.close()
#
# print("Converting " + str(len(tweet_json["tweets"])) + " tweets to vec...")
# tweet_vecs = [dv.get_vec(tweet).tolist() for tweet in tweet_json["tweets"]]
#
# vec_json = {"tweets": tweet_vecs}
# vec_str = json.dumps(vec_json, indent=2)
# file = open("../Tweets/before_train_doc2vec.json", "w+")
# file.write(vec_str)
# file.close()

# print("Training...")
# knn = KMeansNeighbour(tweet_vecs, 2, 0, False)
# knn.train()
#
# print("Testing...")
# for i in range(len(tweet_vecs)):
#     cluster = knn.get_cluster(tweet_vecs[i])
#     print(str(tweet_json["tweets"][i]) + " " + str(cluster))
