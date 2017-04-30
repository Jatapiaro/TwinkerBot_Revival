EN_WHITELIST = '0123456789abcdefghijklmnopqrstuvwxyz '
import numpy as np
from random import sample
import pickle
'''
 split data into train (70%), test (15%) and valid(15%)
    return tuple( (trainX, trainY), (testX,testY), (validX,validY) )

'''
def split_dataset(x, y, ratio = [0.7, 0.15, 0.15] ):
    # number of examples
    data_len = len(x)
    lens = [ int(data_len*item) for item in ratio ]

    trainX, trainY = x[:lens[0]], y[:lens[0]]
    testX, testY = x[lens[0]:lens[0]+lens[1]], y[lens[0]:lens[0]+lens[1]]
    validX, validY = x[-lens[-1]:], y[-lens[-1]:]

    return (trainX,trainY), (testX,testY), (validX,validY)


'''
 generate batches from dataset
    yield (x_gen, y_gen)

    TODO : fix needed

'''
def batch_gen(x, y, batch_size):
    # infinite while
    while True:
        for i in range(0, len(x), batch_size):
            if (i+1)*batch_size < len(x):
                yield x[i : (i+1)*batch_size ].T, y[i : (i+1)*batch_size ].T

'''
 generate batches, by random sampling a bunch of items
    yield (x_gen, y_gen)

'''
def rand_batch_gen(x, y, batch_size):
    while True:
        sample_idx = sample(list(np.arange(len(x))), batch_size)
        yield x[sample_idx].T, y[sample_idx].T

#'''
# convert indices of alphabets into a string (word)
#    return str(word)
#
#'''
#def decode_word(alpha_seq, idx2alpha):
#    return ''.join([ idx2alpha[alpha] for alpha in alpha_seq if alpha ])
#
#
#'''
# convert indices of phonemes into list of phonemes (as string)
#    return str(phoneme_list)
#
#'''
#def decode_phonemes(pho_seq, idx2pho):
#    return ' '.join( [ idx2pho[pho] for pho in pho_seq if pho ])

def get_metadata():
    with open('datasets/twitter/metadata.pkl', 'rb') as f:
        metadata = pickle.load(f)
    return metadata.get('idx2w'), metadata.get('w2idx'), metadata.get('limit')

'''
 a generic decode function
    inputs : sequence, lookup

'''
def decode(sequence, lookup, separator=''): # 0 used for padding, is ignored
    return separator.join([ lookup[element] for element in sequence if element ])

'''
 encode function
    inputs : sentence, lookup
'''
def encode(sentence, lookup, maxlen, whitelist=EN_WHITELIST, separator=''):
    # to lower case
    sentence = sentence.lower()
    # allow only characters that are on whitelist
    sentence = ''.join( [ ch for ch in sentence if ch in whitelist ] )
    # words to indices
    indices_x = [ token for token in sentence.strip().split(' ') ]
    # clip the sentence to fit model (#words)
    indices_x = indices_x[-maxlen:] if len(indices_x) > maxlen else indices_x
    # zero pad
    idx_x = np.array(pad_seq(indices_x, lookup, maxlen))
    # reshape
    return idx_x.reshape([maxlen, 1])

def pad_seq(seq, lookup, maxlen):
    indices = []
    for word in seq:
        if word in lookup:
            indices.append(lookup[word])
        else:
            indices.append(lookup['unk'])
    return indices + [0]*(maxlen - len(seq))
