# -*- coding: utf-8 -*-
import tweepy#, time, sys

from Configuration.TwitterConfiguration import CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET


def tweet(line):
    api = get_api()
    api.update_status(line)
    #time.sleep(1)


def mentions():
    api,auth = get_api()
    api = tweepy.API(auth)
    m = api.mentions_timeline(count = 10)
    #for men in range(0,len(m)):
         #print (m[men])
    return m


def get_api():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api,auth

def get_tweet_to_fix(id):
    api, auth = get_api()
    id_o = api.get_status(id).in_reply_to_status_id
    #print(id_o)
    return api.get_status(id_o)

def response_to_mention(tw,id,user):
    print ("Answer mention")
    api,auth = get_api()
    api.create_favorite(id)
    api.update_status("@"+str(user) + " " + str(tw), in_reply_to_status_id=id)