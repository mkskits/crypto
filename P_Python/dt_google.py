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

dt_pd_google_daily_un = pd.DataFrame(columns=['Bitcoin', 'isPartial'])
single_frames = {
    # 0: '2009-12-01 2010-01-01',
    # 1: '2010-01-01 2010-02-01',
    # 2: '2010-02-01 2010-03-01',

    0: '2009-12-01 2010-01-01',
    1: '2010-01-01 2010-02-01',
    2: '2010-02-01 2010-03-01',
    3: '2010-03-01 2010-04-01',
    4: '2010-04-01 2010-05-01',
    5: '2010-05-01 2010-06-01',
    6: '2010-06-01 2010-07-01',
    7: '2010-07-01 2010-08-01',
    8: '2010-08-01 2010-09-01',
    9: '2010-09-01 2010-10-01',
    10: '2010-10-01 2010-11-01',
    11: '2010-11-01 2010-12-01',
    12: '2010-12-01 2011-01-01',

    13: '2010-12-01 2011-01-01',
    14: '2011-01-01 2011-02-01',
    15: '2011-02-01 2011-03-01',
    16: '2011-03-01 2011-04-01',
    17: '2011-04-01 2011-05-01',
    18: '2011-05-01 2011-06-01',
    19: '2011-06-01 2011-07-01',
    20: '2011-07-01 2011-08-01',
    21: '2011-08-01 2011-09-01',
    22: '2011-09-01 2011-10-01',
    23: '2011-10-01 2011-11-01',
    24: '2011-11-01 2011-12-01',
    25: '2011-12-01 2012-01-01',

    26: '2011-12-01 2012-01-01',
    27: '2012-01-01 2012-02-01',
    28: '2012-02-01 2012-03-01',
    29: '2012-03-01 2012-04-01',
    30: '2012-04-01 2012-05-01',
    31: '2012-05-01 2012-06-01',
    32: '2012-06-01 2012-07-01',
    33: '2012-07-01 2012-08-01',
    34: '2012-08-01 2012-09-01',
    35: '2012-09-01 2012-10-01',
    36: '2012-10-01 2012-11-01',
    37: '2012-11-01 2012-12-01',
    38: '2012-12-01 2013-01-01',

    39: '2012-12-01 2013-01-01',
    40: '2013-01-01 2013-02-01',
    41: '2013-02-01 2013-03-01',
    42: '2013-03-01 2013-04-01',
    43: '2013-04-01 2013-05-01',
    44: '2013-05-01 2013-06-01',
    45: '2013-06-01 2013-07-01',
    46: '2013-07-01 2013-08-01',
    47: '2013-08-01 2013-09-01',
    48: '2013-09-01 2013-10-01',
    49: '2013-10-01 2013-11-01',
    50: '2013-11-01 2013-12-01',
    51: '2013-12-01 2014-01-01',

    52: '2013-12-01 2014-01-01',
    53: '2014-01-01 2014-02-01',
    54: '2014-02-01 2014-03-01',
    55: '2014-03-01 2014-04-01',
    56: '2014-04-01 2014-05-01',
    57: '2014-05-01 2014-06-01',
    58: '2014-06-01 2014-07-01',
    59: '2014-07-01 2014-08-01',
    60: '2014-08-01 2014-09-01',
    61: '2014-09-01 2014-10-01',
    62: '2014-10-01 2014-11-01',
    63: '2014-11-01 2014-12-01',
    64: '2014-12-01 2015-01-01',

    65: '2014-12-01 2015-01-01',
    66: '2015-01-01 2015-02-01',
    67: '2015-02-01 2015-03-01',
    68: '2015-03-01 2015-04-01',
    69: '2015-04-01 2015-05-01',
    70: '2015-05-01 2015-06-01',
    71: '2015-06-01 2015-07-01',
    72: '2015-07-01 2015-08-01',
    73: '2015-08-01 2015-09-01',
    74: '2015-09-01 2015-10-01',
    75: '2015-10-01 2015-11-01',
    76: '2015-11-01 2015-12-01',
    77: '2015-12-01 2016-01-01',

    78: '2015-12-01 2016-01-01',
    79: '2016-01-01 2016-02-01',
    80: '2016-02-01 2016-03-01',
    81: '2016-03-01 2016-04-01',
    82: '2016-04-01 2016-05-01',
    83: '2016-05-01 2016-06-01',
    84: '2016-06-01 2016-07-01',
    85: '2016-07-01 2016-08-01',
    86: '2016-08-01 2016-09-01',
    87: '2016-09-01 2016-10-01',
    88: '2016-10-01 2016-11-01',
    89: '2016-11-01 2016-12-01',
    90: '2016-12-01 2017-01-01',

    91: '2016-12-01 2017-01-01',
    92: '2017-01-01 2017-02-01',
    93: '2017-02-01 2017-03-01',
    94: '2017-03-01 2017-04-01',
    95: '2017-04-01 2017-05-01',
    96: '2017-05-01 2017-06-01',
    97: '2017-06-01 2017-07-01',
    98: '2017-07-01 2017-08-01',
    99: '2017-08-01 2017-09-01',
    100: '2017-09-01 2017-10-01',
    101: '2017-10-01 2017-11-01',
    # 102: '2017-11-01 2017-12-01',
    # 103: '2017-12-01 2018-01-01',
         }

for x in single_frames:
    pytrends.build_payload(kw_list, cat=0, timeframe=single_frames[x], geo='', gprop='')
    dt_pd_google_tmp = pytrends.interest_over_time()
    if x > 0:
        print('x>0')
        if dt_pd_google_tmp.head(1).index == dt_pd_google_daily_un.tail(1).index:
            print('consistency check good')
            lda = dt_pd_google_tmp.head(1)['Bitcoin'] - dt_pd_google_daily_un.tail(1)['Bitcoin']
            lda = float(lda)
            print(lda)
            dt_pd_google_tmp['Bitcoin'] = dt_pd_google_tmp['Bitcoin'] - lda
            dt_pd_google_daily_un = dt_pd_google_daily_un.append(dt_pd_google_tmp)
        else:
            print('consistency check bad')
    else:
        print('x = 0')
        dt_pd_google_daily_un = dt_pd_google_daily_un.append(dt_pd_google_tmp)
    print('retrieve frame', x, 'done')

dt_pd_google_daily = dt_pd_google_daily_un.groupby(dt_pd_google_daily_un.index).first()
dt_pd_google_daily.rename(columns={'Bitcoin': 'google_tr'}, inplace=True)
dt_pd_google_daily['google_tr_fd'] = dt_pd_google_daily['google_tr'].diff(periods=1)

# MAVG calculation to be done after merged dataset
dt_pd_google_daily['google_tr_MAVG30'] = round(dt_pd_google_daily['google_tr'].rolling(window=30).mean(), 0)

dt_pd_google_daily.to_pickle('dt_pd_google.pickle')

print('Google Trend Download Done')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")