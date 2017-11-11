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

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["Bitcoin"]

single_frames = {
    0: '2010-02-01 2012-02-01',
         }

for x in single_frames:
    pytrends.build_payload(kw_list, cat=0, timeframe=single_frames[x], geo='', gprop='')
    dt_pd_google_testing = pytrends.interest_over_time()
    print('retrieve frame', x, 'done')
dt_pd_google_testing.rename(columns={'Bitcoin': 'google_tr'}, inplace=True)

# top = plt.subplot2grid((1,1), (0,0))
# top.plot(dt_pd_google_testing.index, dt_pd_google_testing['google_tr'])
# top.get_xaxis().set_major_formatter(matplotlib.dates.DateFormatter('%Y-%m-%d'))
# top.get_xaxis().set_minor_formatter(matplotlib.dates.DateFormatter('%Y-%m-%d'))
# top.legend()
# plt.gcf().set_size_inches(15, 8)
# plt.title('google trends - testing')
# plt.show()

print('google trend testing done')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")