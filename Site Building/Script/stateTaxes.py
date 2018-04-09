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
from pandas import ExcelWriter
#from tabulate import tabulate
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

import pandas as pd
df = None#pd.DataFrame(columns=['City', 'State', 'State', 'Local', 'Total', 'Rank'])
url = "https://taxfoundation.org/sales-tax-rates-major-cities-midyear-2017/"

page = urllib2.urlopen(url)
soup = BeautifulSoup(page, "lxml")
table_div = soup.find('div' , {'id':'post-content' })
table = table_div.find_all('tr')
idx = 0
for t in table:
    temp = []
    #print t

    if "<td colspan=\"6\">" in str(t):
        continue
    for a in t:
        #print a
        if str(a) != "\n":
            data = str(a).replace("<th>","").replace("</th>","")
            data = str(data).replace("<td>","").replace("</td>","")
            if "(" in data:
                data = data[:data.find("(")]
            #print data
            temp.append(data.strip())
    #print temp
    if "<th>" in str(t):
        df = pd.DataFrame(columns=temp)
    else:
        df.loc[idx] = temp
        idx+=1
    #break
print df
#table = soup.find_all("table")[0]
#x = table.split("<\tr>")
#df = pd.read_html(str(table))[0]
#print type(table[0])
df.to_csv('C:\Users\pilanisp\Documents\Personal\Sem 4\DDDM\My Project work\csv_cityTax_list.csv', sep='|')
writer = ExcelWriter('csv_cityTax_list.xlsx')
df.to_excel(writer)
writer.save()
#states =df["State"].tolist()
#print states
#df1 = pd.read_csv('C:\Users\pilanisp\Documents\Personal\Sem 4\DDDM\My Project work\csv_cityTax_list.txt', delimiter="|")
#print df1
