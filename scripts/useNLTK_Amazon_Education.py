#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 13:38:31 2018
In class script from CSC495 1/30/2018
@author: Marvin
"""

import nltk
import pandas as pd
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob

amazon_city_file = 'D:\\Users\\Marvin\\Google Drive\\CSC\\CSC495\\Amazon Problem\\city_list.csv'
city_list = pd.read_csv(amazon_city_file, names=['state', 'city', 'MSA', 'is_top_twenty'],
                        sep='|', skiprows=1, na_values=['?'])

data = open('D:\\Users\\Marvin\\Google Drive\\CSC\\CSC495\\Amazon Problem\\AmazonHQ_All.txt',
            encoding='utf-8').read()

sentences = sent_tokenize(data)
results = []


amazon_cities = city_list['city']
amazon_states = city_list['state']
ed_filter = ['education', 'program', 'after school', 'after-school', 'high school', 'K-12', 
             'middle school', 'elementary school']
cs_filter = ['information', 'computer', 'software', 'network', 'database', 'web', 
             'computing', 'programming', 'AI']

for sent in sentences:
    for word in ed_filter:
        if (word in sent):
            results.append(sent)


"""
data = []
for line in file:
    data.append(line)

words = word_tokenize(data)
#print(words)
spread=nltk.FreqDist(words)
spread.plot(50,cumulative=True)

for word, frequency in spread.most_common(100):
    print(u'{};{}'.format(word,frequency))

phrases = TextBlob(data)
good = phrases.noun_phrases
#print(good)
out_file = open('AmazonHQ_nounPhrases.txt', 'w',
                encoding='uf-8')
out_file.write(good)
out_file.close()
"""

