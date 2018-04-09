# -*- coding: utf-8 -*-
"""
Imports data from a CSV into a pandas dataframe
@author: Marvin
"""
import pandas as pd
#Actually imports the data from a CSV while specifying the header names, 
#the separator, how many rows to skip, and the NA values.
#skiprows skips the header row

city_file = 'D:\\Users\\Marvin\\Google Drive\\CSC\\CSC495\\Amazon Problem\\city_list.csv'
city_list = pd.read_csv(city_file, names=['state', 'city', 'MSA', 'is_top_twenty'],
                        sep='|', skiprows=1, na_values=[0])

commute_times_df = city_list
commute_times_df['Average Commute Time'] = 0

city_commute_file = 'D:\\Users\\Marvin\\Google Drive\\CSC\\CSC495\\Amazon Problem\\commute_times_city.csv'
city_commute_df = pd.read_csv(city_commute_file, names=['index','City','Avg Commute Time'], 
                                  sep='|', skiprows=1, na_values=['?'], encoding='latin-1')
#city_commute_df = city_commute_df.drop(['index'], axis=1)

city = []
state = []

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'Washington DC': 'DC',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    'Puerto Rico': 'PR',
}

abbrev_to_state = {v: k for k, v in us_state_abbrev.items()}


state = []
city = []

for index, row in city_commute_df.iterrows():
    temp1 = row['City']
    temp = temp1.split(', ')
    city.append(temp[0])
    state.append(abbrev_to_state[temp[len(temp) - 1]])

city_commute_df['City'] = city
city_commute_df['state'] = state
final_data_frame = pd.DataFrame()
final_data_frame['City'] = city_commute_df['City']
final_data_frame['State'] = city_commute_df['state']
final_data_frame['Avg Commute Time (minutes)'] = city_commute_df['Avg Commute Time']
commute_list = []
flag = 0
for row in commute_times_df.itertuples():
    for row2 in final_data_frame.itertuples():
        temp_city = row2[1]
        temp_state = row2[2]
        temp_amazon_city = str(row[2])
        if ((temp_state == row[1]) and ((temp_city == temp_amazon_city) or (temp_city in temp_amazon_city))):
            commute_list.append(row2[3])
            flag = 1
            break
    if (flag != 1):
        commute_list.append(0)
    flag = 0
            

commute_times_df['Average Commute Time'] = commute_list    

csv_out = 'D:\\Users\\Marvin\\Google Drive\\CSC\\CSC495\\Amazon Problem\\commute_times_amazon_cities.csv'
commute_times_df.to_csv(csv_out, sep='|', na_rep='?', 
        columns=['state', 'city', 'MSA', 'is_top_twenty', 'Average Commute Time'])
