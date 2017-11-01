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

    # os.environ['http_proxy'] = "http://gate-zrh.swissre.com:8080"
    # os.environ['HTTP_PROXY'] = "http://gate-zrh.swissre.com:8080"
    # os.environ['https_proxy'] = "http://gate-zrh.swissre.com:8080"
    # os.environ['HTTPS_PROXY'] = "http://gate-zrh.swissre.com:8080"

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
pytrends.build_payload(kw_list, cat=0, timeframe='2010-01-01 2017-10-31', geo='', gprop='')
dt_pd_google = pytrends.interest_over_time()

dt_pd_google = pd.read_pickle('dt_pd_google.pickle')

dt_pd_google.rename(columns={'Bitcoin': 'google_tr'}, inplace=True)


# dt_pd_google.to_pickle('dt_pd_google_v0.pickle')
# plt.plot(dt_pd_google['Bitcoin'])
# dt_pd_google.rename(columns={'Date': 'date'}, inplace=True)


dt_pd_google.to_pickle('dt_pd_google.pickle')

print('Google Trend Download Done')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")