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

    dt_pd_google_daily_idx = pd.read_pickle('dt_pd_google_daily_idx.pickle')
    dt_pd_google_monthly = pd.read_pickle('dt_pd_google_monthly.pickle')

    # check if monthly start dates are equal 01
    # for x in dt_pd_google_monthly.index:
    for cur_date in dt_pd_google_monthly.index:
        if cur_date.day != 1:
            print(cur_date)
            raise ValueError('monthly start date not equal 01')

    # create empty DataFrame with same indices as dt_pd_google_daily_iplt and fill monthly set
    dt_monthly = pd.DataFrame(index=dt_pd_google_daily_idx.index)
    dt_pd_google_monthly = dt_pd_google_monthly.merge(dt_monthly, left_index=True, right_index=True, how='outer')

    dt_lower_bound = pd.DataFrame(index=[dt_pd_google_daily_idx.index.min(), dt_pd_google_monthly.index.min()]).index.max()

    # drop all rows with dates earlier than lower bound
    for cur_date in dt_pd_google_monthly.index:
        if cur_date < dt_lower_bound:
            print('dropped monthly index', cur_date)
            dt_pd_google_monthly.drop(cur_date, inplace=True)
    for cur_date in dt_pd_google_daily_idx.index:
        if cur_date < dt_lower_bound:
            print('dropped daily index', cur_date)
            dt_pd_google_daily_idx.drop(cur_date, inplace=True)

    dt_upper_bound = pd.DataFrame(index=[dt_pd_google_daily_idx.index.max(), dt_pd_google_monthly.index.max()]).index.min()

    # drop all rows with dates later than upper bound
    for cur_date in dt_pd_google_monthly.index:
        if cur_date > dt_upper_bound:
            print('dropped monthly index', cur_date)
            dt_pd_google_monthly.drop(cur_date, inplace=True)
    for cur_date in dt_pd_google_daily_idx.index:
        if cur_date > dt_upper_bound:
            print('dropped daily index', cur_date)
            dt_pd_google_daily_idx.drop(cur_date, inplace=True)

    # Calculate interpolated index
    d = {'google_tr': [np.nan], 'google_tr_fd': [np.nan]}
    dt_pd_google_daily_iplt = pd.DataFrame(index=dt_pd_google_monthly.index, data=d)
    for cur_date in dt_pd_google_monthly.index:
        if dt_pd_google_monthly['google_tr'].loc[[cur_date]].isnull().any().any():
            temp_t_1 = temp_t_1 + \
                float(dt_pd_google_daily_idx.loc[dt_pd_google_daily_idx.index == cur_date, 'google_tr_fd'].as_matrix())
            print(temp_t_1)
            dt_pd_google_daily_iplt.loc[dt_pd_google_daily_iplt.index == cur_date, 'google_tr'] = \
                temp_t_1
        else:
            dt_pd_google_daily_iplt.loc[dt_pd_google_daily_iplt.index == cur_date, 'google_tr'] =\
                dt_pd_google_monthly.loc[dt_pd_google_monthly.index == cur_date, 'google_tr']
            temp_t_1 = float(dt_pd_google_monthly.loc[dt_pd_google_monthly.index == cur_date, 'google_tr'].as_matrix())
            print(temp_t_1)
            print('iplt monthly level ', dt_pd_google_daily_iplt.loc[dt_pd_google_daily_iplt.index == cur_date, 'google_tr'])

    # abs first differences calculation
    dt_pd_google_daily_iplt['google_tr_fd'] = dt_pd_google_daily_iplt['google_tr'].diff(periods=1)

    # MAVG calculation
    dt_pd_google_daily_iplt['google_tr_MAVG30'] = round(dt_pd_google_daily_iplt['google_tr'].rolling(window=30).mean(), 0)

    dt_pd_google_daily_iplt.to_pickle('dt_pd_google_daily_iplt.pickle')

    print('google daily iplt calculated')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")