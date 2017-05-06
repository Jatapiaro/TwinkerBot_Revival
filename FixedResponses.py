from random import randint
import pickle
import os
from TwitterAPI import *
import time


class FixedResponses:
    dict = {}
    def __init__(self):
        if os.path.isfile("answers.pickle"):
            self.dict = pickle.load(open("answers.pickle", "rb"))
        else:
            self.save_pickle()

    def get_response(self, word):
        w = str(word).lower()
        posible_responses = self.dict[w]
        return posible_responses[randint(0, len(posible_responses) - 1)]

    def append_response(self,key, value):
        key = str(key).lower()
        if self.contains_response(key):
            self.dict[key].append(value.lower())
            self.save_pickle()
        else:
            self.dict[key] = [value.lower()]
            self.save_pickle()

    def save_pickle(self):
        pickle.dump(self.dict, open("answers.pickle", "wb"))
        #self.dict = pickle.load(open("answers.pickle", "rb"))

    def contains_response(self,k):
        return k in self.dict



"""f = float(((60+96)/2) * 0.50) - 70.0
print(str(f))
f += float(80*.25)
print(str(f))
f += float(55*.20)
print(str(f))"""

"""f = float(78 * 0.45) - 70
print(str(f))
f += float(80*.10)
print(str(f))
f += float(70*.25)
print(str(f))
f += float(50*.20)
print(str(f))"""
