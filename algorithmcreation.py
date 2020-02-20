import seaborn as sns
import csv
from random import random,randint
import math
import numpy as np
import sklearn
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
from sklearn import model_selection
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pylab as plb
import matplotlib.pyplot as plt

plt.style.use('ggplot')

dataf_full = pd.read_csv("2019_20fixtures.csv")
dataf = dataf_full.drop(columns=['data__id', 'data__name', 'data__league_id', 'data__is_current_season', 'data__current_round_id',
                                 'data__current_stage_id', 'data__fixtures__data__league_id', 'data__fixtures__data__stage_id',
                                 'data__fixtures__data__weather_report', 'data__fixtures__data__weather_report__icon', 'data__fixtures__data__weather_report__temperature_celcius__unit',
                                 'data__fixtures__data__weather_report__temperature__temp', 'data__fixtures__data__weather_report__temperature__unit',
                                 'data__fixtures__data__weather_report__coordinates__lat', 'data__fixtures__data__weather_report__coordinates__lon',
                                 'data__fixtures__data__weather_report__updated_at', 'data__fixtures__data__commentaries',
                                 'data__fixtures__data__pitch', 'data__fixtures__data__details', 'data__fixtures__data__neutral_venue',
                                 'data__fixtures__data__winning_odds_calculated', 'data__fixtures__data__scores__localteam_pen_score',
                                 'data__fixtures__data__scores__visitorteam_pen_score', 'data__fixtures__data__scores__et_score',
                                 'data__fixtures__data__scores__ps_score', 'data__fixtures__data__time__starting_at__date_time',
                                 'data__fixtures__data__time__starting_at__date', 'data__fixtures__data__time__starting_at__timestamp',
                                 'data__fixtures__data__time__starting_at__timezone', 'data__fixtures__data__time__minute',
                                 'data__fixtures__data__time__second', 'data__fixtures__data__time__added_time',
                                 'data__fixtures__data__time__extra_minute', 'data__fixtures__data__time__injury_time',
                                 'data__fixtures__data__assistants__first_assistant_id', 'data__fixtures__data__assistants__second_assistant_id',
                                 'data__fixtures__data__assistants__fourth_official_id', 'data__fixtures__data__leg', 'data__fixtures__data__colors',
                                 'data__fixtures__data__colors__|', 'data__fixtures__data__colors__|__color',
                                 'data__fixtures__data__colors__|__kit_colors', 'data__fixtures__data__deleted'])


'''
dataf['data__fixtures__data__weather_report__code'] = pd.Categorical(dataf['data__fixtures__data__weather_report__code'])
dataf['data__fixtures__data__weather_report__code'] = dataf.data__fixtures__data__weather_report__code.cat.codes

dataf['data__fixtures__data__weather_report__type'] = pd.Categorical(dataf['data__fixtures__data__weather_report__type'])
dataf['data__fixtures__data__weather_report__type'] = dataf.data__fixtures__data__weather_report__type.cat.codes

dataf['data__fixtures__data__weather_report__temperature_celcius__temp'] = pd.Categorical(dataf['data__fixtures__data__weather_report__temperature_celcius__temp'])
dataf['data__fixtures__data__weather_report__temperature_celcius__temp'] = dataf.data__fixtures__data__weather_report__temperature_celcius__temp.cat.codes

dataf['data__fixtures__data__weather_report__temperature_celcius__temp'] = pd.Categorical(dataf['data__fixtures__data__weather_report__temperature_celcius__temp'])
dataf['data__fixtures__data__weather_report__temperature_celcius__temp'] = dataf.data__fixtures__data__weather_report__temperature_celcius__temp.cat.codes

dataf['data__fixtures__data__weather_report__temperature_celcius__temp'] = pd.Categorical(dataf['data__fixtures__data__weather_report__temperature_celcius__temp'])
dataf['data__fixtures__data__weather_report__temperature_celcius__temp'] = dataf.data__fixtures__data__weather_report__temperature_celcius__temp.cat.codes

dataf['data__fixtures__data__weather_report__temperature_celcius__temp'] = pd.Categorical(dataf['data__fixtures__data__weather_report__temperature_celcius__temp'])
dataf['data__fixtures__data__weather_report__temperature_celcius__temp'] = dataf.data__fixtures__data__weather_report__temperature_celcius__temp.cat.codes
'''


print(dataf_prep)
