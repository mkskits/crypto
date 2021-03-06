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

def main():
    print("First Module's Name: {}".format(__name__))
    print('OS:', os.name)
    os.chdir('..')

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    ## INPUT
    ## name of datafile 'fin-assets.csv'
    dt_csv_fin = 'fin-assets.csv'

    dt_pd_fin = pd.read_csv(os.path.abspath(os.curdir) + sl + 'D_Data' + sl + 'B_Bloomberg' + sl + dt_csv_fin)
    dt_pd_fin.rename(columns={'Date': 'date'}, inplace=True)
    dt_pd_fin['date'] = pd.to_datetime(dt_pd_fin['date'], errors='raise', format='%d.%m.%Y', exact='True')
    dt_pd_fin.set_index('date', inplace=True, drop=True, append=False, verify_integrity=True)
    # dt_pd_fin.columns = ['xyz']
    # dt_pd_fin['xyz'] = dt_pd_fin['xyz'].diff(periods=1)
    # dt_pd_fin['xyz_MAVG30'] = round(dt_pd_fin['xyz'].rolling(window=30).mean(), 0)

    # dt_pd_wiki.sort_index(inplace=True, ascending=False)

    # Store pickle to disk
    os.chdir(os.path.abspath(os.curdir) + sl +"P_Python" + sl)
    dt_pd_fin.to_pickle('dt_pd_fin.pickle')

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")


