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
import time

print(os.getcwd())

def daterange(start, end):
    if start < end:
        for n in range((end - start).days + 1):
            yield(start + dt.timedelta(n))
    else:
        for n in range((start - end).days + 1):
            yield(start - dt.timedelta(n))

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

start = dt.date(2010, 7, 18)
# end = (dt.date(2012, 7, 18) + dt.timedelta(days=0))
end = (dt.date.today() + dt.timedelta(days=-5))
ddates = daterange(start, end)

t = 0
single_frames = []

dt_pd_google_dchanges = pd.DataFrame(index=pd.DatetimeIndex(ddates), columns = ['Bitcoin'])
dt_pd_google_dchanges.index.names = ['date']

for date in daterange(start, end):
    single_frames.append(date.isoformat() + ' ' + (date + dt.timedelta(days=1)).isoformat())
    t = t + 1

p = 1
for x in single_frames:
    pytrends.build_payload(kw_list, cat=0, timeframe=x, geo='', gprop='')
    dt_pd_google_testing = pytrends.interest_over_time()
    dt_pd_google_dchanges.loc[dt_pd_google_testing.iloc[1].name] =\
        (dt_pd_google_testing.iloc[1]-dt_pd_google_testing.iloc[0])/dt_pd_google_testing.iloc[0]
    # print((dt_pd_google_testing.iloc[1]-dt_pd_google_testing.iloc[0])/dt_pd_google_testing.iloc[0])
    print('retrieve frame', x, 'done', int(p)/int(t)/100,'%')
    p = p + 1

dt_pd_google_testing.rename(columns={'Bitcoin': 'google_tr'}, inplace=True)
dt_pd_google_dchanges.rename(columns={'Bitcoin': 'google_tr_dchanges'}, inplace=True)

# top = plt.subplot2grid((1,1), (0,0))
# top.plot(dt_pd_google_testing.index, dt_pd_google_testing['google_tr'])
# top.get_xaxis().set_major_formatter(matplotlib.dates.DateFormatter('%Y-%m-%d'))
# top.get_xaxis().set_minor_formatter(matplotlib.dates.DateFormatter('%Y-%m-%d'))
# top.legend()
# plt.gcf().set_size_inches(15, 8)
# plt.title('google trends - testing')
# plt.show()
print(dt_pd_google_testing)

print('google trend testing done')

if __name__ == '__main__':
    main()

else:
    print("Run From Import")
