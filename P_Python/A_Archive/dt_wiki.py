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
    print('OS:', os.name)
    os.chdir('..')

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    ## INPUT
    ## Name of Data File (WIKIPEDIA)
    dt_csv_wiki = 'pageviews-20150701-20171025.csv'

    dt_pd_wiki = pd.read_csv(os.path.abspath(os.curdir) + sl + "D_Data" + sl + "W_Wikipedia" + sl + dt_csv_wiki)
    dt_pd_wiki.rename(columns={'Date': 'date'}, inplace=True)
    dt_pd_wiki['date'] = pd.to_datetime(dt_pd_wiki['date'], errors='raise', format='%Y-%m-%d', exact='True')
    dt_pd_wiki.set_index('date', inplace=True, drop=True, append=False, verify_integrity=True)
    dt_pd_wiki.columns = ['wikipedia']
    dt_pd_wiki['wikipedia_fd'] = dt_pd_wiki['wikipedia'].diff(periods=1)
    dt_pd_wiki['wikipedia_MAVG30'] = round(dt_pd_wiki['wikipedia'].rolling(window=30).mean(),0)

    # dt_pd_wiki.sort_index(inplace=True, ascending=False)

    # Store pickle to disk
    os.chdir(os.path.abspath(os.curdir) + sl +"P_Python" + sl)
    dt_pd_wiki.to_pickle('dt_pd_wiki.pickle')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")


