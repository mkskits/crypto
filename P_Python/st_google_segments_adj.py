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

# open to pickle
dt_pd_google_segments_adj = pd.read_pickle('dt_pd_google_segments_adj.pickle')

dt_pd_google_segments_adj['google_tr'].astype(int).describe()

print('google trend segments download done')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")