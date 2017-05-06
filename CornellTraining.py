import tensorflow as tf
import numpy as np

# preprocessed data
from datasets.cornell import data
import data_utils
import importlib
importlib.reload(data)

metadata, idx_q, idx_a = data.load_data(PATH='datasets/cornell/')
(trainX, trainY), (testX, testY), (validX, validY) = data_utils.split_dataset(idx_q, idx_a)

# parameters
xseq_len = trainX.shape[-1]
yseq_len = trainY.shape[-1]
batch_size = 16
xvocab_size = len(metadata['idx2w'])
yvocab_size = xvocab_size
emb_dim = 1024

import seq2seq_wrapper


model = seq2seq_wrapper.Seq2Seq(xseq_len=xseq_len,
                               yseq_len=yseq_len,
                               xvocab_size=xvocab_size,
                               yvocab_size=yvocab_size,
                               ckpt_path='ckpt/cornell/',
                               emb_dim=emb_dim,
                               num_layers=3
                               )




val_batch_gen = data_utils.rand_batch_gen(validX, validY, 32)
train_batch_gen = data_utils.rand_batch_gen(trainX, trainY, batch_size)


sessi = model.restore_last_session()
sessi = model.train(train_batch_gen, val_batch_gen,sessi)
#sessi = model.train(train_batch_gen, val_batch_gen)