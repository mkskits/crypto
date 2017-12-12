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

    dt_pd_fin = pd.read_pickle('dt_pd_fin.pickle')

    matplotlib.rcParams.update({'font.size': 16})

    dt_pd_fin.index.name = '' # set index column name to '' disables x_label in plot
    # dt_pd_fin[['log.XAU', 'log.Global.Govt']].plot(subplots=True, color='blue', figsize=(8, 6))
    f, (ax1, ax2) = plt.subplots(2, 1, sharex=True, sharey=False)
    ax1.plot(dt_pd_fin[['log.SPX']], color='blue', label='S&P 500 Log-Returns')
    ax1.legend(loc='upper left')
    ax2.plot(dt_pd_fin[['log.MXWO']], color='blue', label='MSCI World Log-Returns')
    ax2.legend(loc='upper left')
    # set size of overall figure not needed here
    plt.gcf().set_size_inches(9, 8)
    # auto-format of x-axis labels & rotation
    f.autofmt_xdate()
    f.tight_layout(pad=0.01)
    dt_pd_fin.index.name = 'date' # re-name index column

    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + sl + "F_Figs" + sl)

    plt.savefig('pt_eq_index_log_ret.pdf')

    # plt.show() disabled / set by global variable in IDE
    # plt.show()

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")