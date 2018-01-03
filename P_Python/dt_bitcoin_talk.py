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

# this scripts takes the raw csv dump from bitcointalk.org (forum activity data) and creates
# a python pickle that is stored to the disk subsequently

def main():
    print("First Module's Name: {}".format(__name__))
    print('OS:', os.name)
    os.chdir('..')

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    ## INPUT
    ## Name of Data File (bitcoin talk)
    dt_bitcoin_talk = 'dt_bitcoin_talk_dump.csv'

    dt_pd_bitcoin_talk = pd.read_csv(os.path.abspath(os.curdir) + sl + "D_Data" + sl + "B_Bitcoin_Talk" + sl + dt_bitcoin_talk)
    dt_pd_bitcoin_talk.rename(columns={'Date': 'date'}, inplace=True)
    dt_pd_bitcoin_talk.rename(columns={'New Topics': 'new_topics', 'New Posts' : 'new_posts',
                                       'New Members' : 'new_members'}, inplace=True)

    dt_pd_bitcoin_talk.set_index(pd.to_datetime(dt_pd_bitcoin_talk['date'], errors='raise', format='%d.%m.%y', exact='True')
                                 , inplace=True, verify_integrity=True)

    dt_pd_bitcoin_talk = dt_pd_bitcoin_talk.drop('date', 1)

    dt_pd_bitcoin_talk.sort_index(inplace=True, ascending=True)

    dt_pd_bitcoin_talk['new_posts_fd'] = dt_pd_bitcoin_talk['new_posts'].diff(periods=1)
    dt_pd_bitcoin_talk['new_posts_MAVG30'] = round(dt_pd_bitcoin_talk['new_posts'].rolling(window=30).mean(),0)

    dt_pd_bitcoin_talk.sort_index(inplace=True, ascending=True)
    dt_pd_bitcoin_talk['log_rtn_new_posts'] = np.log(dt_pd_bitcoin_talk['new_posts'] /
                                                 dt_pd_bitcoin_talk['new_posts'].shift() )

    # Store pickle to disk
    os.chdir(os.path.abspath(os.curdir) + sl +"P_Python" + sl)
    dt_pd_bitcoin_talk.to_pickle('dt_pd_bitcoin_talk.pickle')

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")


