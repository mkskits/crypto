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
# reads / formats data from bitinfo twitter data dump

def main():
    print("First Module's Name: {}".format(__name__))
    print("Module Name: {}".format(__name__))
    print('OS:', os.name)
    os.chdir('..')

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    # INPUT
    # name of the data file
    dt_twitter_bitinfo_file = 'source_bitinfocharts.txt'
    dt_twitter_bitinfo = open(os.path.abspath(os.curdir) + sl + "D_Data" + sl + "T_Twitter" + sl
                              + dt_twitter_bitinfo_file, 'r').read()

    df = []
    labels = ['date', 'tweets']
    rows = dt_twitter_bitinfo.split(",[")
    for line in rows:
        line = str.replace(str.replace(str.replace(line[10:-1],'")',''),'"',''),']','')
        line = line.split(',')
        print(line)
        if line[1] == 'null':
            line[1] = lastlook
        line[1] = float(line[1])
        lastlook = line[1]
        df.append(line)
        #dt_pd_twitter.append(line)
        #print(line)

    dt_pd_twitter_bitinfo = pd.DataFrame.from_records(df, columns = labels)
    dt_pd_twitter_bitinfo.set_index(pd.to_datetime(dt_pd_twitter_bitinfo['date']), inplace=True,
                                                   drop=True, append=False, verify_integrity=True)
    dt_pd_twitter_bitinfo = dt_pd_twitter_bitinfo.drop('date', 1)

    # Store pickle to disk
    os.chdir(os.path.abspath(os.curdir) + sl + "P_Python" + sl)
    dt_pd_twitter_bitinfo.to_pickle('dt_pd_twitter_bitinfo.pickle')
    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + sl + 'D_Data')
    dt_pd_twitter_bitinfo.to_csv('dt_twitter.csv', sep=',')

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':


    main()
else:
    print("Run From Import")


