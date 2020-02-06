from __future__ import absolute_import, division, print_function, unicode_literals
import pymongo
import pandas as pd
import tensorflow_datasets as tfds
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

def plot(historical, metrics):
    plt.plot(historical.historical[metrics])
    plt.plot(historical.historical['val_'+metrics], '')
    plt.xlabel("Epochs")
    plt.ylabel(metrics)
    plt.legend([metrics, 'val_'+metric])
    plt.show()

dataf = pd.read_csv("2019_20fixtures.csv")

dataf['Date'] = pd.Categorical(dataf['Date'])
dataf['Date'] = dataf.Date.cat.codes

dataf['HomeTeam'] = pd.Categorical(dataf['HomeTeam'])
dataf['HomeTeam'] = dataf.HomeTeam.cat.codes

dataf['AwayTeam'] = pd.Categorical(dataf['AwayTeam'])
dataf['AwayTeam'] = dataf.AwayTeam.cat.codes

dataf['FTR'] = pd.Categorical(dataf['FTR'])
dataf['FTR'] = dataf.FTR.cat.codes

dataf['HTR'] = pd.Categorical(dataf['HTR'])
dataf['HTR'] = dataf.HTR.cat.codes

dataf['Referee'] = pd.Categorical(dataf['Referee'])
dataf['Referee'] = dataf.Referee.cat.codes

targets = dataf.pop('FTR', '')
irrelevant = dataf.pop('Div', 'HTR')

full_dataset = tf.data.Dataset.from_tensor_slices((dataf.values, target.values))

#for feat, targ in full_dataset.take(10):
#    print('Features: {}, Target: {}'.format(feat,targ))

#print(tf.constant(dataf['Referee']))

training_set = full_dataset.shuffle(len(dataf)).batch(1)

def create_model():
    model = tf.keras.Sequential([

    ])
#print(full_dataset)