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

print(os.getcwd())

def main():
    print("First Module's Name: {}".format(__name__))
    print("Module Name: {}".format(__name__))
    print('OS:', os.name)
    os.chdir('..')

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    ## INPUT
    ## Name of Data File (Bloomberg)
    dt_csv_xbt_com = 'price.csv'
    dt_pd_xbt_com = pd.read_csv(os.path.abspath(os.curdir) + sl + "D_Data" + sl + "B_Bitcoin_com" + sl + dt_csv_xbt_com)
    # Code to rename single column
    # dt_pd_xbt_bbg.rename(columns={'date': 'Date'}, inplace=True)
    dt_pd_xbt_com['Date'] = pd.to_datetime(dt_pd_xbt_com['Date'], errors='raise', format='%d.%m.%y', exact='True')
    dt_pd_xbt_com.set_index('Date', inplace=True, drop=True, append=False, verify_integrity=True)
    dt_pd_xbt_com.index.name = 'date'
    dt_pd_xbt_com.columns = ['price_usd']
    dt_pd_xbt_com['price_usd_fd'] = dt_pd_xbt_com['price_usd'].diff(periods=1)
    dt_pd_xbt_com['price_usd_MAVG30'] = round(dt_pd_xbt_com['price_usd'].rolling(window=30).mean(),0)

    # dt_pd_wiki.sort_index(inplace=True, ascending=False)

    # Store pickle to disk
    os.chdir(os.path.abspath(os.curdir) + sl + "P_Python" + sl)
    dt_pd_xbt_com.to_pickle('dt_pd_xbt_com.pickle')

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':


    main()
else:
    print("Run From Import")


