import numpy as np

import data_utils
import datetime
import seq2seq_wrapper
import os
import time

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
# load data from pickle and npy files
idx2w, w2idx, limit = data_utils.get_metadata()

# parameters
xseq_len = limit['maxq']
yseq_len = limit['maxa']
batch_size = 1
xvocab_size = len(idx2w)
yvocab_size = xvocab_size
emb_dim = 1024


print('>> Initializing model')
model = seq2seq_wrapper.Seq2Seq(xseq_len=xseq_len,
                               yseq_len=yseq_len,
                               xvocab_size=xvocab_size,
                               yvocab_size=yvocab_size,
                               ckpt_path='ckpt/twitter/',
                               emb_dim=emb_dim,
                               num_layers=3
                               )

print('\n>> Loading pretrained model')
sess = model.restore_last_session()
print('>> Initialization complete; call respond(msg)')
output_file = open("list.txt", 'a')
if os.path.exists("list.txt"):
    print("Found")

while(True):
    line = input("Write: ")
    bot = str(respond(line))
    file_out = "-Human: ["+line+"] ; Bot answer ["+bot+"] ; " +\
               str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    output_file.write(file_out+'\n')
    print(bot)


