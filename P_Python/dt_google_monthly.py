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
    os.chdir('..')

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

# timezone 360 = US CST
pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["Bitcoin"]
# pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
# Specific time is UTC
# pytrends.build_payload(kw_list, cat=0, timeframe='2017-02-06T10 2017-02-12T07', geo='', gprop='')
# date format YYYY-DD-MM
pytrends.build_payload(kw_list, cat=0, timeframe='2010-06-01 2017-11-30', geo='', gprop='')
dt_pd_google_monthly = pytrends.interest_over_time()

dt_pd_google_monthly.rename(columns={'Bitcoin': 'google_tr'}, inplace=True)
dt_pd_google_monthly = dt_pd_google_monthly.drop('isPartial', 1)
# dt_pd_google['google_tr_fd'] = dt_pd_google['google_tr'].diff(periods=1)
# dt_pd_google['google_tr_MAVG30'] = round(dt_pd_google['google_tr'].rolling(window=30).mean(), 0)

dt_pd_google_monthly.to_pickle('dt_pd_google_monthly.pickle')

print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")