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

    dt_pd_xbt_bbg = pd.read_pickle('dt_pd_xbt_com.pickle')
    dt_pd_google = pd.read_pickle('dt_pd_google_segments_adj.pickle')
    dt_pd_wiki = pd.read_pickle('dt_pd_wiki.pickle')

    dt_pd_aggr = dt_pd_xbt_bbg.merge(dt_pd_wiki, left_index=True, right_index=True, how='inner').merge(dt_pd_google,
        left_index=True, right_index=True, how='inner')

    dt_pd_aggr.to_pickle('dt_pd_aggr.pickle')

    print('Data aggr run done')

if __name__ == '__main__':
        main()
else:
        print("Run From Import")
