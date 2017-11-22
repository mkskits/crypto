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

    dt_pd_aggr = pd.read_pickle('dt_pd_aggr.pickle')

    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + sl + 'D_Data')

    dt_pd_aggr.to_csv('dt_aggregated.csv', sep=',')

    print('data aggr run done')

if __name__ == '__main__':
        main()
else:
        print("Run From Import")
