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

    dt_pd_xbt_com = pd.read_pickle('dt_pd_xbt_com.pickle')
    dt_pd_xbt_com = dt_pd_xbt_com[dt_pd_xbt_com.price_usd != 0]
    dt_pd_xbt_com['segment'] = 1
    # calculate log returns
    dt_pd_xbt_com['xbt_log_ret'] = np.log(dt_pd_xbt_com['price_usd'] / dt_pd_xbt_com['price_usd'].shift(1))
    # calculate annualized volatility based on 30day rolling window
    dt_pd_xbt_com['xbt_vol_30d_ann'] = dt_pd_xbt_com['xbt_log_ret'].rolling(window=30, center=False).std() * np.sqrt(365)

    matplotlib.rcParams.update({'font.size': 16})

    dt_pd_xbt_com.index.name = ''
    dt_pd_xbt_com[['price_usd', 'xbt_vol_30d_ann']].plot(subplots=True, color='blue', figsize=(8, 6), legend=True)
    dt_pd_xbt_com.index.name = 'date'

    plt.gcf().set_size_inches(9, 8)

    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + sl + "F_Figs" + sl)
    layout = plt.tight_layout(pad=0.01)
    plt.savefig('pt_xbt_com_std.pdf')

    # plt.show() not needed due to global variable setting in pyCharm
    # plt.show()

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")