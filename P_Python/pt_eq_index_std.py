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

    # data source - financial asset price series from bloomberg / processed with R / stored as pickle by ??
    dt_pd_fin = pd.read_pickle('dt_pd_fin.pickle')

    matplotlib.rcParams.update({'font.size': 16})

    dt_pd_fin.index.name = ''

    f, (ax1, ax2) = plt.subplots(2, 1, sharex=True, sharey=False)
    ax1.plot(dt_pd_fin[['SPX']], color='blue', label='SPX')
    ax1.legend(loc='upper left')
    ax1b = ax1.twinx()
    ax1b.plot(dt_pd_fin[['MXWO']], color='red', label='MXWO')
    ax1b.legend(loc='upper right')
    ax2.plot(dt_pd_fin[['SPX.vol']], color='blue', label='$\sigma_{SPX}$')
    ax2.legend(loc='upper left')
    ax2b = ax2.twinx()
    ax2b.plot(dt_pd_fin[['MXWO.vol']], color='red', label='$\sigma_{MXWO}$')
    ax2b.legend(loc='upper right')
    dt_pd_fin.index.name = 'date'

    # set size of overall figure not needed here
    plt.gcf().set_size_inches(9, 8)
    # auto-format of x-axis labels & rotation
    f.autofmt_xdate()

    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + sl + "F_Figs" + sl)
    # layout = plt.tight_layout(pad=0.01)
    f.tight_layout(pad=0.01)
    plt.savefig('pt_eq_index_std.pdf')

    # plt.show() not needed due to global variable setting in pyCharm
    # plt.show()

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")