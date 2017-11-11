import os
import scipy
print('scipy: %s' % scipy.__version__)
import numpy as np
print('numpy: %s' % np.__version__)
import matplotlib
print('matplotlib: %s' % matplotlib.__version__)
import matplotlib.pyplot as plt
import pandas as pd
print('pandas: %s' % pd.__version__)
import pandas_datareader.data as web
import datetime as dt
from datetime import datetime
import sklearn
# import statsmodels
from pandas import Series
import pickle
import pyflux as pf
# %matplotlib inline

print(os.getcwd())

# class Object(object): pass
#
# pd.core.indexes = Object()
# pd.core.indexes.datetimes = Object()
# pd.core.indexes.datetimes.DatetimeIndex = pd.DatetimeIndex

def main():
    print("First Module's Name: {}".format(__name__))

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'


    # tickers = ['NYSE:JPM', 'NYSE:GS', 'NYSE:C', 'NYSE:WFC', 'NYSE:MS', 'TSE:BNS', 'NYSE:TD', 'NYSE:NMR', 'NYSE:DB', 'LON:BARC',
              # 'NYSE:HSBC','NYSE:UBS', 'NYSE:CS', 'EPA:BNP', 'EPA:GLE', 'EPA:ACA', 'EPA:KN']
    tickers = ['NYSE:JPM', 'NYSE:GS', 'NYSE:C', 'NYSE:WFC', 'NYSE:MS']

    start = dt.datetime(2010, 1, 1)
    end = dt.datetime(2017, 10, 31)
    stocks = web.DataReader(tickers, 'google', start, end)
    closing_prices = np.log(stocks.Close)
    closing_pt = stocks.Close
    # plt.figure(figsize=(15, 5))
    # plt.plot(closing_pt.index, closing_pt)
    # plt.legend(closing_pt.columns.values, loc=3)
    # plt.title("Closing price")

    y = pf.VAR(data=closing_prices, lags=2, integ=1)
    x = y.fit()
    x.summary()

    # Plot latent variables
    # y.plot_z(list(range(0, 6)), figsize=(15, 5))

    # Predictions vs fitted (in-sample fit)
    # y.plot_fit(figsize=(15, 5))

    # Predictions Chart (bandwidth)
    # y.plot_predict(past_values=19, h=5, figsize=(15, 5))

    # Predictions Table
    # y.predict(h=5)

    # Rolling out of sample predictions
    y.plot_predict_is(h=30, figsize=((15, 5)))

    print('VAR v1 done')

if __name__ == '__main__':
        main()
else:
        print("Run From Import")