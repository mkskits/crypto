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
import pyperclip
import json
import io

print(os.getcwd())

# script description
# this script imports the financial data from the R-pre-processed csv file and stores
# the python pickle object

def main():
    print("First Module's Name: {}".format(__name__))
    print("Module Name: {}".format(__name__))
    print('OS:', os.name)

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    # INPUT
    dt_pd_twitter_bitinfo = pd.read_pickle('dt_pd_twitter_bitinfo.pickle')
    dt_pd_twitter_bitinfo.rename(columns={'tweets': 'nTweets'}, inplace=True)

    dt_pd_cts_twitter = pd.read_pickle('dt_pd_cts_twitter.pickle')

    dt_pd_twitter_aggr = dt_pd_twitter_bitinfo
    dt_pd_twitter_aggr = dt_pd_twitter_aggr.append(dt_pd_cts_twitter)

    dt_pd_twitter_aggr.sort_index(ascending=True, inplace=True)

    # Store pickle to disk
    dt_pd_twitter_aggr.to_pickle('dt_pd_twitter_aggr.pickle')

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':


    main()
else:
    print("Run From Import")


