from random import randint
import pickle
import os
from TwitterAPI import *
import time
from random import randint

class LearningUsers:
    dict = {}

    def __init__(self):
        if os.path.isfile("users.pickle"):
            self.dict = pickle.load(open("users.pickle", "rb"))
        else:
            self.save_pickle()


    def append_like(self,key, value):
        key = str(key)
        if self.contains_user(key):
            for x in range(0,len(value)):
                self.dict[key].append(value[x].lower())
            self.save_pickle()
        else:
            self.dict[key] = [value.lower()]
            self.save_pickle()

    def what_do_i_like(self,id):
        likes = self.dict[id]
        if len(likes)!=1:
            lik = 'You like: '
            usedn = []
            nlikes = randint(1, 3)
            for x in range(0, nlikes):
                if x == len(likes)-1:
                    return lik
                else:
                    r = -1
                    while True:
                        r = randint(1, len(likes)-1)
                        if r not in usedn:
                            break
                    lik += likes[r] +" , "
                    usedn.append(r)
            return lik
        else:
            return "Tell me what do you like"

    def save_pickle(self):
        pickle.dump(self.dict, open("users.pickle", "wb"))

    def contains_user(self,k):
        return k in self.dict


