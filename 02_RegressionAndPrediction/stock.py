#!/usr/bin/python3

import pandas as pd
from alpha_vantage.timeseries import TimeSeries
#import alpha_vantage
import matplotlib.pyplot as plt
import time

# Api key to access alpha vantage stock data
api_key = "RUNKI8FWHBYTQE4K"

stockIndx='AAPL'
ts = TimeSeries(key=api_key, output_format='pandas')
#data, meta_data = ts.get_intraday(symbol="MSFT", interval='1min', outputsize ='full')
#data, meta_data = ts.get_monthly(symbol="MSFT")
data, meta_data = ts.get_monthly(symbol=stockIndx)

def plotPerChange():
    close_data = data['4. close']
    percentage_change = close_data.pct_change()
    percentage_change = percentage_change.cumsum()
    plt.figure()
    percentage_change.plot( label=stockIndx, color='red');
    plt.legend()
    plt.show()

def plotAbsData():
    close_data = data['4. close']
    #close_data = close_data.cumsum()
    plt.figure()
    close_data.plot( label=stockIndx, color='red');
    plt.legend()
    plt.show()

#data, meta_data = ts.get_intraday(symbol="MSFT", interval='1min', outputsize ='full')
def writeExcel():
    data.to_excel("output.xlsx")

plotAbsData()
#plotPerChange()
