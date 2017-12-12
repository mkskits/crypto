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
    dt_pd_fin[['DXY.fd', 'log.DXY']].plot(subplots=True, color='blue', figsize=(8, 6))
    dt_pd_fin.index.name = 'date' # re-name index column

    plt.gcf().set_size_inches(9, 8)

    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + sl + "F_Figs" + sl)
    layout = plt.tight_layout(pad=0.01)
    plt.savefig('pt_dxy_fd_log_ret.pdf')

    # plt.show() disabled / set by global variable in IDE
    # plt.show()

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")