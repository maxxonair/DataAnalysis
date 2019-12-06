import pandas as pd
from alpha_vantage.timeseries import TimeSeries
#import alpha_vantage
import matplotlib.pyplot as plt
import time

# Api key to access alpha vantage stock data
api_key = "RUNKI8FWHBYTQE4K"
#gapminder = pd.read_csv(data_url)
#print(gapminder.head(300))

def createPercentageComp(stockIndx1, stockIndx2, relativeChange):
    ts = TimeSeries(key=api_key, output_format='pandas')
    #data, meta_data = ts.get_intraday(symbol="MSFT", interval='1min', outputsize ='full')
    data, meta_data = ts.get_monthly(symbol=stockIndx1)
    close_data = data['4. close']
    percentage_change = close_data.pct_change()

    ts2 = TimeSeries(key=api_key, output_format='pandas')
    data2, meta_data = ts2.get_monthly(symbol=stockIndx2)
    close_data2 = data2['4. close']
    percentage_change2 = close_data2.pct_change()
    if(relativeChange):
        percentage_change = percentage_change.cumsum()
        percentage_change2 = percentage_change2.cumsum()
        plt.figure();
        percentage_change.plot( label="MSFT", color='blue');
        percentage_change2.plot( label="AAPL", color='red');
        plt.legend()
        plt.show()
    else:
                plt.figure();
                close_data.plot( label="MSFT", color='blue');
                close_data2.plot( label="AAPL", color='red');
                plt.legend()
                plt.show()

createPercentageComp("MSFT","AAPL", False)
