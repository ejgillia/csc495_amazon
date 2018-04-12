# -*- coding: utf-8 -*-
"""
Imports data from a CSV into a pandas dataframe
@author: Marvin
"""
import pandas as pd
import math
#Actually imports the data from a CSV while specifying the header names, 
#the separator, how many rows to skip, and the NA values.
#skiprows skips the header row

education_data = 'D:\\Users\\Marvin\\Google Drive\\CSC\\CSC495\\Amazon Problem\\Data USA College Degree by County and Name\\Data USA Cart.csv'
education_df = pd.read_csv(education_data, names=['Name', 'geo_sumlevel','geo_id',
                                'Degree','cip_sumlevel','cip_id', 'grads_total_2013',
                                'grads_total_2014','grads_total_2015'],
                        sep=',', skiprows=1, na_values=[0])
education_df = education_df.drop(['geo_id','grads_total_2013',
                                'grads_total_2014', 'cip_sumlevel','cip_id'], axis=1)
amazon_city_file = 'D:\\Users\\Marvin\\Google Drive\\CSC\\CSC495\\Amazon Problem\\city_list.csv'
city_list = pd.read_csv(amazon_city_file, names=['state', 'city', 'MSA', 'is_top_twenty'],
                        sep='|', skiprows=1, na_values=['?'])

education_df_places = education_df.loc[education_df['geo_sumlevel'] == 'place']
#city_commute_df = city_commute_df.drop(['index'], axis=1)

cs_filter = ['information', 'computer', 'software', 'network', 'database', 'web', 'computing']

education_df_filtered_place_degree = education_df_places.loc[education_df_places['Degree'].str.contains('|'.join(cs_filter), case=False)]


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

for index, row in education_df_filtered_place_degree.iterrows():
    temp1 = row['Name']
    temp = temp1.split(', ')
    city.append(temp[0])
    for item in temp:
        if len(item) == 2:
            state.append(abbrev_to_state[item])
        
education_df_filtered_place_degree['City'] = city
education_df_filtered_place_degree['State'] = state

grads_sum = []

for city in city_list.itertuples():
    rel_state = city[1]
    rel_city = city[2]
    grads = 0
    for row in education_df_filtered_place_degree.itertuples():
        num_grads = 0
        temp_city = row[5]
        temp_state = row[6]
        if ((temp_state == rel_state) and ((temp_city == rel_city) or (temp_city in rel_city))):
            num_grads = row[4]
            if (not math.isnan(num_grads)):
                grads += num_grads
            
    grads_sum.append(grads)

city_list['Total Graduates'] = grads_sum

csv_out = 'D:\\Users\Marvin\\Git\\csc495_amazon\\total_graduates_amazon_cities.csv'
city_list.to_csv(csv_out, sep='|', na_rep='?', 
        columns=['state', 'city', 'MSA', 'is_top_twenty', 'Total Graduates'])
#for row in education_df_filtered_place_degree.iterrows():
    


        

        
    
    

