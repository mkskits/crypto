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

    ax = plt.subplot(111)

    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    dt_pd_google[dt_pd_google.segment.isin(list)].groupby('segment').plot(y='google_tr',
                                                                              kind='line', ax=ax)
    L = plt.legend()
    _ = [plt.setp(item, 'text', T) for item, T in zip(L.texts, list)]


    # colors = dt_pd_google['segment']
    # top = plt.subplot2grid((4,4), (0,0), rowspan=3, colspan=4)
    # top.plot(dt_pd_google.index, dt_pd_google['google_tr'])
    # top.legend()
    # plt.gcf().set_size_inches(8, 8)
    # plt.title('Monthly Bitcoin Google Trend Index and First Differences')
    plt.gcf().set_size_inches(15, 8)

    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + sl + "F_Figs" + sl)
    plt.savefig('pt_google_tr_segments_unadj.pdf')

    plt.show()

    print('Plotting Google Trend monthly done')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")