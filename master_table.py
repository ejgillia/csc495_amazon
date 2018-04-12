#!/usr/bin/python3

import pandas as pd


filenames = ["commute_times_amazon_cities.csv", "cities_anshul.csv"]

logistics_base_filepath = ["Logistics"]
logistics = ["State-City-MSA - Airport Connectivity to Major Hubs.csv",
		"State-City-MSA - Airport Travel Time.csv",
		"State-City-MSA - Inrix Traffic Index.csv",
		"State-City-MSA - Public Transit Score.csv"
		"State-City-MSA - Statewise Highway and Road Length.csv"]

site_building_base_filepath = ["Site Building/Data"]
site_building = ["csv_cityTax_list.csv", "statewise_cnbc_ranking.csv"]

df = pd.read_csv("csv_city_list.csv", sep = "|")



for f in filenames:
	print(f)
	tba = pd.read_csv(f, sep = "|", encoding='latin-1')
	print(tba.columns)
	print(df.columns)

	df = pd.merge(df, tba, how = "left", on = ["city", "state", "is_top_twenty", "MSA"])

tba = pd.read_csv("Logistics/State-City-MSA - Airport Connectivity to Major Hubs.csv", sep = "|", encoding='latin-1')
df = pd.merge(df, tba, how = "left", on = ["city", "state"])
#del df["MSA_y"]
del df["Unnamed: 7"]
del df["Unnamed: 8"]
del df["Unnamed: 9"]
del df["Unnamed: 10"]

tba = pd.read_csv("Logistics/State-City-MSA - Airport Travel Time.csv", sep = "|", encoding='latin-1')
df = pd.merge(df, tba, how = "left", on = ["city", "state"])
#del df["MSA"]
del df["Unnamed: 4"]
del df["Unnamed: 5"]
del df["Unnamed: 6"]
del df["Unnamed: 7"]
del df["Unnamed: 8"]
del df["Unnamed: 9"]
del df["Unnamed: 10"]

tba = pd.read_csv("Logistics/State-City-MSA - Inrix Traffic Index.csv", sep = "|", encoding='latin-1')
df = pd.merge(df, tba, how = "left", on = ["city", "state"])
del df["Unnamed: 9"]
del df["Unnamed: 10"]

tba = pd.read_csv("Logistics/State-City-MSA - Public Transit Score.csv", sep = "|", encoding='latin-1')
df = pd.merge(df, tba,how = "left",  on = ["city", "state"])
del df["Unnamed: 4"]
del df["Unnamed: 5"]
del df["Unnamed: 6"]
del df["Unnamed: 7"]
del df["Unnamed: 8"]
del df["Unnamed: 9"]
del df["Unnamed: 10"]

tba = pd.read_csv("Logistics/State-City-MSA - Statewise Highway and Road Length.csv", sep = "|", encoding='latin-1')
df = pd.merge(df, tba, how = "left", on = ["city", "state"])
del df["Unnamed: 5"]
del df["Unnamed: 6"]
del df["Unnamed: 7"]
del df["Unnamed: 8"]
del df["Unnamed: 9"]
del df["Unnamed: 10"]


#only an overlap of 32
#tba = pd.read_csv("Site Building/Data/csv_cityTax_list.csv", sep = "|", encoding='latin-1')
#df = pd.merge(df, tba, on = ["city", "state"])

tba = pd.read_csv("Site Building/Data/statewise_cnbc_ranking.csv", sep = "|", encoding='latin-1')
df = pd.merge(df, tba, how='left', on='state')
del df["Unnamed: 0"]
del df["MSA_x"]
del df["MSA_y"]
df.to_csv("master.csv", sep='|')







