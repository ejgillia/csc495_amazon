# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv
import pprint as pp
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd
import urllib2
#from tabulate import tabulate
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys



url = "https://www.cnbc.com/2017/07/11/americas-top-states-for-business-2017-overall-ranking.html"

page = urllib2.urlopen(url)
soup = BeautifulSoup(page, "lxml")

table = soup.find_all("table")[0]
df = pd.read_html(str(table))[0]
print df
states =df["State"].tolist()
print states
df1 = pd.read_csv('C:\Users\pilanisp\Documents\Personal\Sem 4\DDDM\My Project work\csv_city_list.txt', delimiter="|")
print df1
