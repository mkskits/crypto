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
import datetime as dt
import pickle
import pytrends
import lxml
from pytrends.request import TrendReq

print(os.getcwd())

def main():
    print("First Module's Name: {}".format(__name__))
    print('OS:', os.name)

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    dt_pd_google_daily_idx = pd.read_pickle('dt_pd_google_daily.pickle')

    # drop unused / outdated columns
    dt_pd_google_daily_idx.drop(['google_tr_fd', 'google_tr_MAVG30'], axis=1, level=None, inplace=True, errors='raise')

    # 'normalize' index to 100
    dt_pd_google_daily_idx['google_tr'] = dt_pd_google_daily_idx / dt_pd_google_daily_idx.loc[dt_pd_google_daily_idx['google_tr'].idxmax()]['google_tr'] * 100

    # abs first differences calculation
    dt_pd_google_daily_idx['google_tr_fd'] = dt_pd_google_daily_idx['google_tr'].diff(periods=1)

    # MAVG calculation
    dt_pd_google_daily_idx['google_tr_MAVG30'] = round(dt_pd_google_daily_idx['google_tr'].rolling(window=30).mean(), 0)

    # store pd as pickle
    dt_pd_google_daily_idx.to_pickle('dt_pd_google_daily_idx.pickle')

    print('Google Trend daily idx Done')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")