import os
import json


class TweetRepository:
    def __init__(self, data_source):
        self.__data_source = data_source
        self.__tweets_list = None

    def get_all_tweets(self):
        self.__populate_tweets_from_file()
        return self.__tweets_list

    def __populate_tweets_from_file(self):
        if self.__tweets_list is None:
            if not os.path.exists(self.__data_source):
                self.__tweets_list = []
            else:
                output_file_read = open(self.__data_source, "r+")
                self.__tweets_list = json.loads(output_file_read.read())["tweets"]
                output_file_read.close()
