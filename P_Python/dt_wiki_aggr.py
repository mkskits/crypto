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

    # 1) Open legacy pickle files aggregated through dt_pd_wiki_legacy_slow.py (stored in D_Data/W_Wikipedia/L_legacy_pickles
    os.chdir(os.path.abspath(os.curdir) + sl + 'D_Data' + sl + 'W_Wikipedia' + sl + 'L_legay-pickles' + sl)

    dt_pickles = []
    with open('dt_wiki_pickles.ini') as f:
        dt_pickles = f.read().splitlines()
        f.close()

    # set up empty pandas dataframe to append the single pickles into
    dt_pd_wiki_pk = pd.DataFrame(columns=['project', 'page_title', 'counter', 'rsize', 'tstamp'])
    dt_pd_wiki_pk.set_index('page_title', inplace=True, drop=True, append=False, verify_integrity=True)

    for dt_pickle_pk in dt_pickles:
        print('dt_pickle:', dt_pickle_pk)
        dt_pd_wiki_pk = dt_pd_wiki_pk.append(pd.read_pickle(dt_pickle_pk))

    dt_pd_wiki_pk = dt_pd_wiki_pk[dt_pd_wiki_pk.project=='en']
    dt_pd_wiki_pk = dt_pd_wiki_pk.drop('rsize', 1)
    dt_pd_wiki_pk = dt_pd_wiki_pk.drop('project', 1)
    dt_pd_wiki = dt_pd_wiki_pk

    # 2) Open CSV dump and append to pandas dataframe (source: https://tools.wmflabs.org/pageviews/)
    # Name of Data File (WIKIPEDIA)
    # import of the csv data dump from https://tools.wmflabs.org/pageviews (available from 1st July 2015 onwards)
    dt_csv_wiki = 'pageviews-20150701-20180112.csv'
    os.chdir('..')
    dt_pd_wiki_csv = pd.read_csv(os.path.abspath(os.curdir) + sl + dt_csv_wiki)
    dt_pd_wiki_csv.rename(columns={'Date': 'tstamp'}, inplace=True)
    dt_pd_wiki_csv.rename(columns={'Bitcoin': 'counter'}, inplace=True)
    dt_pd_wiki_csv.rename(columns={'Bitcoin': 'counter'}, inplace=True)
    dt_pd_wiki_csv['tstamp'] = pd.to_datetime(dt_pd_wiki_csv['tstamp'], errors='raise', format='%Y-%m-%d', exact='True')
    dt_pd_wiki_csv['page'] = 'Bitcoin'
    # verify_integrity = False as index will have duplicates, which is expected
    dt_pd_wiki_csv.set_index('page', inplace=True, drop=True, append=False, verify_integrity=False)

    # append dt_pd_wiki_csv to dt_pd_wiki
    dt_pd_wiki = dt_pd_wiki.append(dt_pd_wiki_csv)

    # 3) Open / process grep outputs and append to pandas data frame
    os.chdir(os.path.abspath(os.curdir) + sl + 'L_legay-pickles' + sl)
    dt_wiki_grep = []
    with open('dt_wiki_grepdt.ini') as f:
        dt_wiki_grep = f.read().splitlines()
        f.close()

    dt_pd_wiki_grep = pd.DataFrame(columns=['tstamp', 'page_title', 'counter', 'rsize'])
    for dt_grep_file in dt_wiki_grep:
        print("dt_grep:", dt_grep_file)
        dt_pd_wiki_grep = dt_pd_wiki_grep.append(pd.read_table(dt_grep_file, sep=' ', usecols=[0, 1, 2, 3],
                                        names=['tstamp', 'page_title', 'counter', 'rsize']))
    dt_pd_wiki_grep['tstamp'] = dt_pd_wiki_grep['tstamp'].str.slice(13, 26)
    dt_pd_wiki_grep['tstamp'] = pd.to_datetime(dt_pd_wiki_grep['tstamp'], errors='raise',
                                            format='%Y%m%d-%H%M', exact='True')
    dt_pd_wiki_grep.set_index('page_title', inplace=True, drop=True, append=False, verify_integrity=False)
    dt_pd_wiki_grep['project'] = 'en'
    dt_pd_wiki_grep = dt_pd_wiki_grep.drop('project', 1)
    dt_pd_wiki_grep = dt_pd_wiki_grep.drop('rsize', 1)
    dt_pd_wiki_grep.index.rename('', inplace=True)

    dt_pd_wiki = dt_pd_wiki.append(dt_pd_wiki_grep)

    # aggregation
    dt_pd_wiki.sort_values('tstamp', ascending=True)
    dt_pd_wiki = dt_pd_wiki.groupby(dt_pd_wiki.tstamp).first()
    dt_pd_wiki = dt_pd_wiki.astype(float)
    dt_pd_wiki = dt_pd_wiki.resample('D').sum()

    dt_pd_wiki.columns = ['wikipedia']

    # outliers & number formatting
    mask = dt_pd_wiki.wikipedia > 150000
    column_name = 'wikipedia'
    dt_pd_wiki.loc[mask, column_name] = 150000
    dt_pd_wiki['wikipedia'].fillna(value=0, inplace=True)

    # store pickle to disk
    os.chdir('..' + sl + '..' + sl + '..' + sl + 'P_Python' + sl)
    dt_pd_wiki.to_pickle('dt_pd_wiki.pickle')

    # test plot
    dt_pd_wiki.plot()

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")


