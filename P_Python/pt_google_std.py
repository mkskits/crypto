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
import sklearn
# import statsmodels
from pandas import Series
import datetime as dt
import pickle
import pylab

print(os.getcwd())

def main():
    print("First Module's Name: {}".format(__name__))

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    dt_google = pd.read_pickle('dt_pd_google_btc_daily.pickle')
    # calculate log returns
    dt_google['google_log_ret'] = np.log(dt_google['google_tr_btc'] / dt_google['google_tr_btc'].shift(1))
    # calculate annualized volatility based on 30day rolling window
    dt_google['google_vol_30d_ann'] = dt_google['google_log_ret'].rolling(window=30, center=False).std() * np.sqrt(365)

    matplotlib.rcParams.update({'font.size': 16})

    dt_google.index.name = ''
    dt_google.rename(columns={'google_tr_btc': 'Google', 'google_vol_30d_ann' : '$\sigma_{30D}$' }, inplace=True)
    dt_google[['Google Trends Index', '$\sigma_{30D}$']].plot(subplots=True, color='blue', figsize=(8, 6), legend=True)
    dt_google.index.name = 'date'

    plt.gcf().set_size_inches(9, 8)

    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + sl + "F_Figs" + sl)
    layout = plt.tight_layout(pad=0.01)
    plt.savefig('pt_google_std.pdf')

    # plt.show() not needed due to global variable setting in pyCharm
    # plt.show()

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")