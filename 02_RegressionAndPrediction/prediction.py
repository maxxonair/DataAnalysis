
import quandl
import numpy as np
#from sklearn.linear_model import LinearRegression
#from sklearn.svm import SVR
#from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt 




#Get the stock data
df = quandl.get("WIKI/AMZN")
#df = quandl.get("WIKI/BNG")
# Take a look at the data
#print(df.head())

df = df[['Adj. Close']]

forecast_out = 30 #'n=30' days
#Create another column (the target or dependent variable) shifted 'n' units up
df['Prediction'] = df[['Adj. Close']].shift(-forecast_out)
#print the new data set
print(df.tail())
