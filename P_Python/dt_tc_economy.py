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
from pandas import Series
import datetime as dt
import pickle

print(os.getcwd())

# this scripts takes the raw csv input generated from the blockchain analysis script (ctc-user_stats_base.py)
# and creates python pickle that is stored to the disk subsequently

def main():
    print("First Module's Name: {}".format(__name__))
    print('OS:', os.name)
    os.chdir('..')

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    ## INPUT
    ## Name of Data File (bitcoin economy)
    dt_bitcoin_economy = 'C-bitcoin-user_stats_base-heur_8ci_3.day.csv'

    dt_pd_bitcoin_economy = pd.read_csv(os.path.abspath(os.curdir) + sl + "D_Data" + sl + "C_Blockchain" + sl + dt_bitcoin_economy)
    dt_pd_bitcoin_economy.rename(columns={'time': 'date'}, inplace=True)

    dt_pd_bitcoin_economy.set_index(pd.to_datetime(dt_pd_bitcoin_economy['date'], errors='raise', exact='True')
                                 , inplace=True, verify_integrity=True)

    dt_pd_bitcoin_economy = dt_pd_bitcoin_economy.drop('date', 1)

    dt_pd_bitcoin_economy.sort_index(inplace=True, ascending=True)

    # Store pickle to disk
    os.chdir(os.path.abspath(os.curdir) + sl +"P_Python" + sl)
    dt_pd_bitcoin_economy.to_pickle('dt_pd_bitcoin_economy.pickle')

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")


