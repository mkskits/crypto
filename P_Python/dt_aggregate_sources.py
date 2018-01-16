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

print(os.getcwd())

def main():
    print("First Module's Name: {}".format(__name__))

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    dt_pd_xbt_com = pd.read_pickle('dt_pd_xbt_com.pickle')
    dt_pd_google = pd.read_pickle('dt_pd_google_btc_daily.pickle')
    dt_pd_wiki = pd.read_pickle('dt_pd_wiki.pickle')
    dt_pd_bitcoin_talk = pd.read_pickle('dt_pd_bitcoin_talk.pickle')
    dt_pd_fin = pd.read_pickle('dt_pd_fin.pickle')
    dt_pd_userstats = pd.read_pickle('dt_pd_bitcoin_economy.pickle')
    # dt_pd_twitter_bitinfo = pd.read_pickle('dt_pd_twitter_bitinfo.pickle')
    # dt_pd_cts_twitter = pd.read_pickle('dt_pd_cts_twitter.pickle')
    dt_pd_twitter_aggr = pd.read_pickle('dt_pd_twitter_aggr.pickle')

    dt_pd_aggr = dt_pd_xbt_com.merge(dt_pd_wiki, left_index=True, right_index=True, how='inner').merge(dt_pd_google,
        left_index=True, right_index=True, how='inner')

    dt_pd_aggr = dt_pd_aggr.merge(dt_pd_fin, left_index=True, right_index=True, how='inner')
    dt_pd_aggr = dt_pd_aggr.merge(dt_pd_bitcoin_talk, left_index=True, right_index=True, how='inner')
    dt_pd_aggr = dt_pd_aggr.merge(dt_pd_userstats, left_index=True, right_index=True, how='inner')
    # dt_pd_aggr = dt_pd_aggr.merge(dt_pd_twitter_bitinfo, left_index=True, right_index=True, how='inner')
    # dt_pd_aggr = dt_pd_aggr.merge(dt_pd_cts_twitter, left_index=True, right_index=True, how='inner')
    # append twitter to aggregate
    dt_pd_aggr = dt_pd_aggr.merge(dt_pd_twitter_aggr, left_index=True, right_index=True, how='inner')
    dt_pd_aggr.index.name = 'date'

    # store aggr data as pickle and CSV file
    dt_pd_aggr.to_pickle('dt_pd_aggregated.pickle')
    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + sl + 'D_Data')
    dt_pd_aggr.to_csv('dt_aggregated.csv', sep=',')

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
        main()
else:
        print("Run From Import")
