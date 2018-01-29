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
import pylab

print(os.getcwd())

def main():
    print("First Module's Name: {}".format(__name__))

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    # data source - financial asset price series from bloomberg / processed with R / stored as pickle by dt_fin.py
    dt_pd_twitter = pd.read_pickle('dt_pd_twitter_bitinfo.pickle')

    dt_pd_twitter['twitter_log_ret'] = np.log(dt_pd_twitter['tweets'] / dt_pd_twitter['tweets'].shift(1))
    # calculate annualized volatility based on 30day rolling window
    dt_pd_twitter['twitter_fd'] = dt_pd_twitter['tweets'] - dt_pd_twitter['tweets'].shift(1)

    matplotlib.rcParams.update({'font.size': 16})

    dt_pd_twitter.index.name = ''

    f, (ax1, ax2) = plt.subplots(2, 1, sharex=True, sharey=False)
    ax1.plot(dt_pd_twitter[['twitter_fd']], color='blue', label='First Differences (abs)')
    ax1.legend(loc='upper left')
    # ax1b = ax1.twinx()
    # ax1b.plot(dt_pd_fin[['Global.Govt']], color='red', label='GA Treasuries')
    # ax1b.legend(loc='upper right')
    ax2.plot(dt_pd_twitter[['twitter_log_ret']], color='blue', label='First Differences (Log)')
    ax2.legend(loc='upper right')
    # ax2.legend(loc='upper left')
    # ax2b = ax2.twinx()
    # ax2b.plot(dt_pd_fin[['Global.Govt.vol']], color='red', label='$\sigma_{GA Treasuries}$')
    # ax2b.legend(loc='upper right')
    dt_pd_twitter.index.name = 'date'

    # set size of overall figure not needed here
    plt.gcf().set_size_inches(9, 8)
    # auto-format of x-axis labels & rotation
    f.autofmt_xdate()

    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + sl + "F_Figs" + sl)
    # layout = plt.tight_layout(pad=0.01)
    f.tight_layout(pad=0.01)
    plt.savefig('pt_twitter_fd.pdf')

    # plt.show() not needed due to global variable setting in pyCharm

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")