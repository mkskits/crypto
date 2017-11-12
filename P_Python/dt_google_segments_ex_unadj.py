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
    0: '2017-08-01 2017-08-31',
    1: '2017-09-01 2017-09-30',
    2: '2017-08-01 2017-09-30',
}

z = 1
dt_pd_google_segments = pd.DataFrame(columns = ['Bitcoin', 'segment'])
for x in single_frames:
    pytrends.build_payload(kw_list, cat=0, timeframe=single_frames[x], geo='', gprop='')
    dt_pd_google_tmp = pytrends.interest_over_time()
    print(x)
    if x > 0:
        print('x>0')
        dt_pd_google_tmp['segment'] = x
        dt_pd_google_segments = dt_pd_google_segments.append(dt_pd_google_tmp)
    else:
        print('x = 0')
        dt_pd_google_tmp['segment'] = x
        dt_pd_google_segments = dt_pd_google_segments.append(dt_pd_google_tmp)
    print('retrieve frame', x, 'done - ', z/len(single_frames)*100,'%')
    z = z + 1

# dt_pd_google_daily = dt_pd_google_daily_un.groupby(dt_pd_google_daily_un.index).first()
dt_pd_google_segments.rename(columns={'Bitcoin': 'google_tr'}, inplace=True)

dt_pd_google_segments.to_pickle('dt_pd_google_ex_unadj.pickle')

print('google trend ex download done')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")