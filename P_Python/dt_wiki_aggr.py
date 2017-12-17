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

    # 1) Open legacy pickle files aggregated through dt_pd_wiki_legacy.py (stored in D_Data/W_Wikipedia/L_legacy_pickles
    os.chdir(os.path.abspath(os.curdir) + sl + 'D_Data' + sl + 'W_Wikipedia' + sl + 'L_legay-pickles' + sl)

    dt_pickles = []
    with open('dt_wiki_pickles.ini') as f:
        dt_pickles = f.read().splitlines()
        f.close()

    # set up empty pandas dataframe to append the single pickles into
    dt_pd_wiki = pd.DataFrame(columns=['project', 'page_title', 'counter', 'rsize', 'tstamp'])
    dt_pd_wiki.set_index('page_title', inplace=True, drop=True, append=False, verify_integrity=True)

    for dt_pickle in dt_pickles:
        print('dt_pickle:', dt_pickle)
        dt_pd_wiki = dt_pd_wiki.append(pd.read_pickle(dt_pickle))


    # 2) Open CSV dump and append to pandas dataframe (source: https://tools.wmflabs.org/pageviews/)
    # Name of Data File (WIKIPEDIA)
    # import of the csv data dump from https://tools.wmflabs.org/pageviews (available from 1st July 2015 onwards)
    dt_csv_wiki = 'pageviews-20150701-20171130.csv'
    os.chdir('..')
    dt_pd_wiki_csv = pd.read_csv(os.path.abspath(os.curdir) + sl + dt_csv_wiki)
    dt_pd_wiki_csv.rename(columns={'Date': 'tstamp'}, inplace=True)
    dt_pd_wiki_csv.rename(columns={'Bitcoin': 'counter'}, inplace=True)
    dt_pd_wiki_csv.rename(columns={'Bitcoin': 'counter'}, inplace=True)
    dt_pd_wiki_csv['tstamp'] = pd.to_datetime(dt_pd_wiki_csv['tstamp'], errors='raise', format='%Y-%m-%d', exact='True')
    dt_pd_wiki_csv['page'] = 'Bitcoin'
    # verify_integrity = False as index will have duplicates, which is expected
    dt_pd_wiki_csv.set_index('page', inplace=True, drop=True, append=False, verify_integrity=False)
    dt_pd_wiki_csv['project'] = 'en'
    dt_pd_wiki_csv['rsize'] = 0

    # append dt_pd_wiki_csv to dt_pd_wiki
    dt_pd_wiki = dt_pd_wiki.append(dt_pd_wiki_csv)

    # 3) Open / process grep outputs and append to pandas data frame
    os.chdir(os.path.abspath(os.curdir) + sl + 'L_legay-pickles' + sl)
    dt_wiki_grep = []
    with open('dt_wiki_grepdt.ini') as f:
        dt_wiki_grep = f.read().splitlines()
        f.close()




    # dt_pd_wiki_csv.columns = ['wikipedia']
    # dt_pd_wiki_csv['wikipedia_fd'] = dt_pd_wiki['wikipedia'].diff(periods=1)
    # dt_pd_wiki_csv['wikipedia_MAVG30'] = round(dt_pd_wiki['wikipedia'].rolling(window=30).mean(),0)
    # dt_pd_wiki.sort_index(inplace=True, ascending=False)

    # Store pickle to disk
    os.chdir(os.path.abspath(os.curdir) + sl +"P_Python" + sl)
    dt_pd_wiki.to_pickle('dt_pd_wiki.pickle')

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")

