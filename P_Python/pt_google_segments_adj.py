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

    dt_pd_google = pd.read_pickle('dt_pd_google_segments_adj.pickle')

    matplotlib.rcParams.update({'font.size': 16})

    gs = matplotlib.gridspec.GridSpec(2, 1,
                           width_ratios=[4],
                           height_ratios=[4, 6]
                                      )
    ax = plt.subplot(gs[0])

    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    list2 = ['2010-07-18 2011-04-04',
             '2010-11-25 2011-08-12',
             '2011-04-04 2011-12-20',
             '2011-08-12 2012-04-28',
             '2011-12-20 2012-09-05',
             '2012-04-28 2013-01-13',
             '2012-09-05 2013-05-23',
             '2013-01-13 2013-09-30',
             '2013-05-23 2014-02-07',
             '2013-09-30 2014-06-17',
             '2014-02-07 2014-10-25',
             '2014-06-17 2015-03-04',
             '2014-10-25 2015-07-12',
             '2015-03-04 2015-11-19',
             '2015-07-12 2016-03-28',
             '2015-11-19 2016-08-05',
             '2016-03-28 2016-12-13',
             '2016-08-05 2017-04-22',
             '2016-12-13 2017-08-30',
             '2017-04-22 2018-01-07',
    ]

    dt_pd_google[dt_pd_google.segment.isin(list)].groupby('segment').plot(y='google_tr',
                                                                              kind='line', ax=ax)
    L = plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), fancybox=True, shadow=True, ncol=2)
    _ = [plt.setp(item, 'text', T) for item, T in zip(L.texts, list2)]

    plt.gcf().set_size_inches(9, 8)

    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + sl + "F_Figs" + sl)
    plt.savefig('pt_google_tr_segments_adj.pdf')

    plt.show()

    print('Plotting Google Trend monthly done')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")