import numpy as np

import datautils as data_utils
import seq2seq_wrapper
import os
import time
from TwitterAPI import *
from FixedResponses import FixedResponses
from random import choices
from string import ascii_uppercase,digits
from random import randint
import datetime

correction_hash = lambda N: ''.join(choices(ascii_uppercase + digits, k=N))


def print_to_file(user,bot):
    output_file = open("realconversations.txt", 'a')
    if os.path.exists("realconversations.txt"):
        print("Found")
    file_out = "-Human: [" + user + "] ; Bot answer [" + bot + "] ; " + \
               str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    output_file.write(file_out + '\n')
'''
    interface
'''
def respond(msg):
    encoded_msg = data_utils.encode(msg, w2idx, limit['maxq'])
    response = model.predict(sess, encoded_msg)[0]
    return data_utils.decode(response, idx2w)


'''
    init
'''
print('>> Initializing data')
dm = str(input("Input data model: ")).lower()

# load data from pickle and npy files
if dm == 'twitter':
    idx2w, w2idx, limit = data_utils.get_metadata()
else:
    idx2w, w2idx, limit = data_utils.get_metadata2()

# parameters
xseq_len = limit['maxq']
yseq_len = limit['maxa']
batch_size = 64
xvocab_size = len(idx2w)
yvocab_size = xvocab_size
emb_dim = 1024


print('>> Initializing model')

model = seq2seq_wrapper.Seq2Seq(xseq_len=xseq_len,
                               yseq_len=yseq_len,
                               xvocab_size=xvocab_size,
                               yvocab_size=yvocab_size,
                               ckpt_path='ckpt/'+dm+'/',
                               emb_dim=emb_dim,
                               num_layers=3
                               )

print('\n>> Loading pretrained model')
sess = model.restore_last_session()
print('>> Initialization complete; call respond(msg)')


hash = correction_hash(randint(5,7))
print("My hash: "+str(hash))
fixed = FixedResponses()
while True:
    ment = mentions()
    for x in range(0, len(ment)):
        if ment[x].favorite_count != 0:
            continue
        else:
            line = str(ment[x].text).split(' ', 1)[1]
            if hash.lower() in line.lower():
                key = get_tweet_to_fix(ment[x].in_reply_to_status_id).text.split(' ', 1)[1]
                value = ment[x].text.split(hash)[1]
                print("Key"+str(key)+", Value: "+str(value))
                fixed.append_response(str(key).replace(" +"," "),str(value).replace(" +"," "))
                response_to_mention("Ok", ment[x].id, ment[x].author.screen_name)
                hash = correction_hash(randint(5,7))
            elif fixed.contains_response(line):
                r = fixed.get_response(line)
                response_to_mention(r, ment[x].id, ment[x].author.screen_name)
            else:
                bot = str(respond(line.lower().replace("'","").replace(
                    ","," ").replace(" +",' ')))
                print_to_file(line, bot)
                response_to_mention(bot, ment[x].id, ment[x].author.screen_name)
    print("My hash: " + str(hash))
    time.sleep(15)






