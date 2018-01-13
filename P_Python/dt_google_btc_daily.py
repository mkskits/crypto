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
        0: '2010-07-01 2011-03-01',
        1: '2011-03-01 2011-11-01',
        2: '2011-11-01 2012-07-01',
        3: '2012-07-01 2013-03-01',
        4: '2013-03-01 2013-11-01',
        5: '2013-11-01 2014-07-01',
        6: '2014-07-01 2015-03-01',
        7: '2015-03-01 2015-11-01',
        8: '2015-11-01 2016-07-01',
        9: '2016-07-01 2017-03-01',
        10: '2017-03-01 2017-11-01',
        11: '2017-11-01 2017-12-12',
    }

    z = 1
    # documentation:
        # dt_pd_google_segments: final pd containing trend data
        # dt_pd_google_tmp: temporary set contatining one single frame, that is appended to pd_google_segments
        # lda = adjustment coefficient
    dt_pd_google_segments = pd.DataFrame(columns = ['Bitcoin', 'segment'])
    for x in single_frames:
        pytrends.build_payload(kw_list, cat=0, timeframe=single_frames[x], geo='', gprop='')
        dt_pd_google_tmp = pytrends.interest_over_time()
        if x > 0:
            print('x>0')
            dt_pd_google_tmp['segment'] = x
            lda = dt_pd_google_tmp['Bitcoin'].head(1) / dt_pd_google_segments['Bitcoin'].tail(1)
            print(lda)
            dt_pd_google_tmp['Bitcoin'] = dt_pd_google_tmp['Bitcoin'] / float(lda)
            dt_pd_google_segments = dt_pd_google_segments.append(dt_pd_google_tmp)
        else:
            print('x = 0')
            dt_pd_google_tmp['segment'] = x
            dt_pd_google_segments = dt_pd_google_segments.append(dt_pd_google_tmp)
        print('retrieve frame', x, 'done - ', z/len(single_frames)*100,'%')
        z = z + 1

    # drop overlapping points
    dt_pd_google_segments['dd'] = dt_pd_google_segments.index
    dt_pd_google_segments.drop_duplicates(subset='dd', keep='first', inplace = True)
    dt_pd_google_segments.drop(['dd'], axis=1, inplace=True)

    # rename column
    dt_pd_google_segments.rename(columns={'Bitcoin': 'google_tr_btc'}, inplace=True)

    # 'normalize' index to 100
    dt_pd_google_segments['google_tr_btc'] = dt_pd_google_segments / \
                                         dt_pd_google_segments.loc[dt_pd_google_segments['google_tr_btc'].idxmax()][
                                              'google_tr_btc'] * 100

    dt_pd_google_segments = dt_pd_google_segments.drop('isPartial', 1)

    # store to pickle
    os.chdir(os.getcwd() + sl + 'P_Python')
    dt_pd_google_segments.to_pickle('dt_pd_google_btc_daily.pickle')

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")