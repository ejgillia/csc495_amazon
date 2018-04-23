import statsmodels.discrete.discrete_model as sm
from sklearn import linear_model, datasets
import pandas as pd
from pandas import ExcelWriter
from sklearn import preprocessing
import math

def userValue(userWeights):

	df = pd.read_csv('dddmfinaldatav0.csv',delimiter = ",")
	df = df.dropna()
	df = df.reset_index(drop=True)


	logreg = linear_model.LogisticRegression(C=1e5)
	temp = df.iloc[:,3:].copy()
	temp = temp.convert_objects(convert_numeric=True)
	temp1 = df.iloc[:,:3].copy()


	x = temp.values #returns a numpy array
	min_max_scaler = preprocessing.MinMaxScaler()
	x_scaled = min_max_scaler.fit_transform(x)
	temp = pd.DataFrame(x_scaled, columns=temp.columns)

	paramlst = ['Infrastructure', 'Growth and Economy', 'Prosperity', 'Human Capital', 'Average Commute Time', 'diversity_rank', 'Travel Time', 'Hours Spent in Congestion', 'PEAK', 'Daytime', 'Technology and Innovation', 'Business Friendly', 'StateTax', 'Local Tax']
	for i in paramlst:
		temp[i] = 1 - temp[i]

	logreg = linear_model.LogisticRegression(C=1e5, fit_intercept=True)
	md1 = logreg.fit(temp,temp1.iloc[:,2])

	paramWeight = {}
	paramNames = temp.columns

	for i in range(len(paramNames)):
		paramWeight[paramNames[i]] = userWeights[i]

	headerList = list(temp.columns)

	cityscore = {}
	citylist = list(temp1['city'])

	scores = []
	counter = 0
	for (id, row) in temp.iterrows():
		total = 0
		for idx, val in enumerate(row):
			total = total + paramWeight[headerList[idx]]*val
		cityscore[citylist[counter]] = total
		scores.append(total)
		counter+=1

	cityscore = sorted(cityscore.items(), key=lambda x: x[1], reverse=True)
	orderedcity =  [x[0] for x in cityscore]
	orderedcityscore = [x[1] for x in cityscore]
	maxPossibleScore = sum(userWeights)
	print(cityscore)
	return zip(orderedcity,orderedcityscore),maxPossibleScore


def ourModel(temp,temp1,myCity):
	dicta = {}

	for i in range(len(temp.columns)):
		dicta[temp.columns[i]] = md1.coef_[0][i]

	dicta['intercept'] = md1.intercept_[0]
	interceptcoefficient = md1.intercept_[0]

	headerList = list(temp.columns)

	cityscore = {}
	cityNameAndIndex = {}
	citylist = list(temp1['city'])

	scores = []
	counter = 0
	for (id, row) in temp.iterrows():
		total = 0
		for idx, val in enumerate(row):

			total = total + (math.exp(dicta[headerList[idx]]) / (1 + math.exp(dicta[headerList[idx]])))*val
		total = total + math.exp(interceptcoefficient) / (1 + math.exp(interceptcoefficient))
		cityscore[citylist[counter]] = total
		scores.append(total)
		cityNameAndIndex[citylist[counter]] = id
		counter+=1

	cityscore = sorted(cityscore.items(), key=lambda x: x[1], reverse=True)
	orderedcity =  [x[0] for x in cityscore]
	orderedcityscore = [x[1] for x in cityscore]
	maxPossibleScore = len(temp.columns)
	topCityIndex = cityNameAndIndex[orderedcity[0]]

	df['Final_Scores'] = scores
	print(cityscore)

	writer = ExcelWriter('Final_ScoresUpdatedColumn.xlsx')
	df.to_excel(writer)
	writer.save()

	if myCity == 1:
		return topCityIndex


def makeMyCityWin(temp,temp1,myCityName,winnerCityId):

	colNames = temp.columns
	cityNameAndIndex = {}
	citylist = list(temp1['city'])	
	counter = 0
	for (id, row) in temp.iterrows():
		cityNameAndIndex[citylist[counter]] = id
		counter+=1

	myCityId = cityNameAndIndex[myCityName]
	myCityParameters = list(temp.loc[myCityId])
	winnerCityParameters = list(temp.loc[winnerCityId])

	toBeImprovedParameters = {}

	for i in range(len(myCityParameters)):
		if winnerCityParameters[i] > myCityParameters[i]:
			toBeImprovedParameters[colNames[i]] = winnerCityParameters[i] - myCityParameters[i]

	toBeImprovedParameters = sorted(toBeImprovedParameters.items(), key=lambda x: x[1], reverse=True)
	paramName =  [x[0] for x in toBeImprovedParameters]
	improveMargin = [x[1] for x in toBeImprovedParameters]

	print(paramName)
	print(improveMargin)



df = pd.read_csv('dddmfinaldatav0.csv',delimiter = ",")
df = df.dropna()
df = df.reset_index(drop=True)


logreg = linear_model.LogisticRegression(C=1e5)
temp = df.iloc[:,3:].copy()
temp = temp.convert_objects(convert_numeric=True)
temp1 = df.iloc[:,:3].copy()


x = temp.values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
temp = pd.DataFrame(x_scaled, columns=temp.columns)

paramlst = ['Infrastructure', 'Growth and Economy', 'Prosperity', 'Human Capital', 'Average Commute Time', 'diversity_rank', 'Travel Time', 'Hours Spent in Congestion', 'PEAK', 'Daytime', 'Technology and Innovation', 'Business Friendly', 'StateTax', 'Local Tax']
for i in paramlst:
	temp[i] = 1 - temp[i]

logreg = linear_model.LogisticRegression(C=1e5, fit_intercept=True)
md1 = logreg.fit(temp,temp1.iloc[:,2])
  

#User Functionality
print("User Functionality Starts")
weightEnteredByUser = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
userValue(weightEnteredByUser)
print("User Functionality Ends\n\n\n")


#Default Functionality for Amazon
print("Model Functionality Starts")
ourModel(temp,temp1,0)
print("Model Functionality Ends\n\n\n")

#Make my city win
print("Make my city win Functionality Starts")
cityName = "Providence - Rhode Island"
makeMyCityWin(temp,temp1,cityName,ourModel(temp,temp1,1))
print("Make my city win Functionality Ends")
