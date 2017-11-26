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

    dt_pd_xbt_com = pd.read_pickle('dt_pd_xbt_com.pickle')
    dt_pd_xbt_com = dt_pd_xbt_com[dt_pd_xbt_com.price_usd != 0]
    dt_pd_xbt_com['segment'] = 1

    matplotlib.rcParams.update({'font.size': 16})

    gs = matplotlib.gridspec.GridSpec(2, 1,
                           width_ratios=[4],
                           height_ratios=[20, 1]
                                      )
    ax = plt.subplot(gs[0])

    list2 = '2010-07-18 - ' + str(dt_pd_xbt_com.tail(1).index.strftime('%Y-%m-%d')[0])
    list = [1]

    dt_pd_xbt_com[dt_pd_xbt_com.segment.isin(list)].groupby('segment').plot(y='price_usd',
                                                                              kind='line', ax=ax)
    L = plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), fancybox=True, shadow=True, ncol=2)
    L.get_texts()[0].set_text(list2)

    plt.gcf().set_size_inches(9, 8)

    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + sl + "F_Figs" + sl)
    plt.savefig('pt_xbt_com.pdf')

    plt.show()

    print('Plotting xbt_com done')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")