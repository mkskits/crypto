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

    dt_pd_google = pd.read_pickle('dt_pd_google_segments_unadj.pickle')

    matplotlib.rcParams.update({'font.size': 16})
    colors = dt_pd_google['segment']
    plt.scatter(dt_pd_google.index, dt_pd_google['google_tr'], c=colors, s=10, alpha=0.8)
    plt.gcf().set_size_inches(9, 8)

    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + sl + "F_Figs" + sl)
    plt.savefig('pt_google_tr_segments_scatter.pdf')

    plt.show()

    print('Plotting Google Trend monthly done')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")