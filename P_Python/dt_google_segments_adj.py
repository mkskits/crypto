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

single_frames = {
    0: '2010-07-18 2011-04-04',
    1: '2010-11-25 2011-08-12',
    2: '2011-04-04 2011-12-20',
    3: '2011-08-12 2012-04-28',
    4: '2011-12-20 2012-09-05',
    5: '2012-04-28 2013-01-13',
    6: '2012-09-05 2013-05-23',
    7: '2013-01-13 2013-09-30',
    8: '2013-05-23 2014-02-07',
    9: '2013-09-30 2014-06-17',
    10: '2014-02-07 2014-10-25',
    11: '2014-06-17 2015-03-04',
    12: '2014-10-25 2015-07-12',
    13: '2015-03-04 2015-11-19',
    14: '2015-07-12 2016-03-28',
    15: '2015-11-19 2016-08-05',
    16: '2016-03-28 2016-12-13',
    17: '2016-08-05 2017-04-22',
    18: '2016-12-13 2017-08-30',
    19: '2017-04-22 2017-11-30',
}

z = 1
# documentation:
    # dt_pd_google_segments: final pd containing trend data
    # dt_pd_google_tmp: temporary set contatining one single frame, that is appended to pd_google_segments
    # lda = mean absolute deviation between
dt_pd_google_segments = pd.DataFrame(columns = ['Bitcoin', 'segment'])
for x in single_frames:
    pytrends.build_payload(kw_list, cat=0, timeframe=single_frames[x], geo='', gprop='')
    dt_pd_google_tmp = pytrends.interest_over_time()
    if x > 0:
        print('x>0')
        dt_pd_google_tmp['segment'] = x
        lda = dt_pd_google_tmp['Bitcoin'] - dt_pd_google_segments['Bitcoin']
        # dt_pd_google_tmp['Bitcoin'] = dt_pd_google_tmp['Bitcoin'] - lda.mean(skipna=True)
        # dt_pd_google_tmp['Bitcoin'] = dt_pd_google_tmp['Bitcoin'] - 10 * lda.mean(skipna=True)
        dt_pd_google_tmp['Bitcoin'] = dt_pd_google_tmp.subtract(lda.mean(skipna=True), fill_value=0)['Bitcoin']
        dt_pd_google_segments = dt_pd_google_segments.append(dt_pd_google_tmp)
    else:
        print('x = 0')
        dt_pd_google_tmp['segment'] = x
        dt_pd_google_segments = dt_pd_google_segments.append(dt_pd_google_tmp)
    print('retrieve frame', x, 'done - ', z/len(single_frames)*100,'%')
    z = z + 1

# drop overlapping points
dt_pd_google_segments = dt_pd_google_segments[dt_pd_google_segments.index.duplicated(keep='first')]
# dt_pd_google_segments.index.drop_duplicates(keep='last')

# rename column
dt_pd_google_segments.rename(columns={'Bitcoin': 'google_tr'}, inplace=True)

# 'normalize' index to 100
dt_pd_google_segments['google_tr'] = dt_pd_google_segments / \
                                      dt_pd_google_segments.loc[dt_pd_google_segments['google_tr'].idxmax()][
                                          'google_tr'] * 100

# fd & mavg calculations
dt_pd_google_segments['google_tr_fd'] = dt_pd_google_segments['google_tr'].diff(periods=1)
dt_pd_google_segments['google_tr_MAVG30'] = round(dt_pd_google_segments['google_tr'].rolling(window=30).mean(), 0)

# store to pickle
dt_pd_google_segments.to_pickle('dt_pd_google_segments_adj.pickle')

print('google trend segments download done')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")