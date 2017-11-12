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

    dt_pd_google = pd.read_pickle('dt_pd_google_ex_unadj.pickle')

    matplotlib.rcParams.update({'font.size': 16})
    ax = plt.subplot(111)

    list = [0, 1]
    list2 = ['2017-08-01 2017-08-31', '2017-09-01 2017-09-30']
    dt_pd_google[dt_pd_google.segment.isin(list)].groupby('segment').plot(y='google_tr',
                                                                              kind='line', ax=ax)
    L = plt.legend()
    _ = [plt.setp(item, 'text', T) for item, T in zip(L.texts, list2)]

    plt.gcf().set_size_inches(9, 8)

    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + sl + "F_Figs" + sl)
    plt.savefig('pt_google_tr_segments_ex_unadj1.pdf')

    plt.show()

    print('Plotting Google Trend monthly done')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")