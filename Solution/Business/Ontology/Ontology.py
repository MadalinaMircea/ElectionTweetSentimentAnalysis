from owlready2 import *


class Ontology:
    def __init__(self, data_source):
        self.__data_source = data_source
        self.__ontology = get_ontology(data_source)
        self.__ontology.load()

    def label(self, token):
        for onto_class in self.__ontology.classes():
            if len(onto_class.descendants()) == 1:
                if token in [class_indiv.name for class_indiv in onto_class.instances()]:
                    return onto_class.name

        return token
