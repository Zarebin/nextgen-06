from typing import *
from sklearn.tree import DecisionTreeClassifier


class Model():
    '''
    #FIXME: implement functions to extract feature vector from a parsed page, 
    '''

    def __init__(self, ): 
        self.model = DecisionTreeClassifier()
        pass


    def fit(self, data):
        self.model.fit(data)