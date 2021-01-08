from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk import FreqDist, pprint
import json


class WordCloudCreator:
    def __init__(self, information):
        self.__background_color = information["background_color"]
        self.__freq_dist = None
        self.__wc = None

        self.__create_wordcloud(information)

    def __create_wordcloud(self, information):
        if information["type"] == "data":
            self.__create_from_data(information)
        elif information["type"] == "json":
            self.__create_from_json(information)
        elif information["type"] == "json_file":
            self.__create_from_json_file(information)

    def __create_from_data(self, information):
        self.__freq_dist = FreqDist(information["data"])
        self.__wc = WordCloud(width=800, height=400, max_words=50,
                              background_color=self.__background_color).generate_from_frequencies(self.__freq_dist)

    def __create_from_json(self, information):
        self.__freq_dist = FreqDist(information["json"][information["property_name"]])
        self.__wc = WordCloud(width=800, height=400, max_words=50,
                              background_color=self.__background_color).generate_from_frequencies(self.__freq_dist)

    def __create_from_json_file(self, information):
        output_file_read = open(information["file_path"], "r+")
        tokens = json.loads(output_file_read.read())["tokens"]
        output_file_read.close()
        self.__freq_dist = FreqDist(tokens)
        self.__wc = WordCloud(width=800, height=400, max_words=50,
                              background_color=self.__background_color).generate_from_frequencies(self.__freq_dist)

    def plot(self):
        plt.figure(figsize=(12, 10))
        plt.imshow(self.__wc, interpolation="bilinear")
        plt.axis("off")
        plt.show()

    def save_to_file(self, output_file):
        self.__wc.to_file(output_file)

    def get_frequencies(self, max_nr):
        return self.__freq_dist.most_common()[:max_nr]
