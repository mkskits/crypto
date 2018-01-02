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
# date format YYYY-MM-DD (trends)

dt_pd_google_daily_un = pd.DataFrame(columns=['Bitcoin', 'isPartial', 'google_tr_log_rtn'])
single_frames = []
with open('google_trend_segments.ini') as f:
    single_frames = f.read().splitlines()
    f.close()
y=0
for x in single_frames:
    pytrends.build_payload(kw_list, cat=0, timeframe=x, geo='', gprop='')
    dt_pd_google_tmp = pytrends.interest_over_time()
    mask = dt_pd_google_tmp.Bitcoin == 0
    column_name = 'Bitcoin'
    dt_pd_google_tmp.loc[mask, column_name] = 1
    dt_pd_google_tmp['google_tr_log_rtn'] = np.log(dt_pd_google_tmp['Bitcoin'] / dt_pd_google_tmp['Bitcoin'].shift(1))
    dt_pd_google_daily_un = dt_pd_google_daily_un.append(dt_pd_google_tmp)
    if y > 0:
        print('x>0')
    else:
        print('y = 0')
        dt_pd_google_daily_un = dt_pd_google_daily_un.append(dt_pd_google_tmp)
    print('retrieve', x, 'done')
    y = y + 1

dt_pd_google_daily = dt_pd_google_daily_un.groupby(dt_pd_google_daily_un.index).first()
dt_pd_google_daily.rename(columns={'Bitcoin': 'google_tr'}, inplace=True)

# abs first differences calculations
# dt_pd_google_daily['google_tr_fd'] = dt_pd_google_daily['google_tr'].diff(periods=1)

# MAVG calculation to be done after merged dataset
# dt_pd_google_daily['google_tr_MAVG30'] = round(dt_pd_google_daily['google_tr'].rolling(window=30).mean(), 0)

dt_pd_google_daily.to_pickle('dt_pd_google_daily.pickle')

print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")