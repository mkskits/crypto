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
import statsmodels
from pandas import Series
import datetime as dt
import pickle
import pylab

print(os.getcwd())

def main():
    print("First Module's Name: {}".format(__name__))

    dt_pd_wiki = pd.read_pickle('dt_pd_wiki.pickle')

    top = plt.subplot2grid((4,4), (0,0), rowspan=3, colspan=4)
    top.plot(dt_pd_wiki.index, dt_pd_wiki['Wikipedia'])
    top.plot(dt_pd_wiki.index, dt_pd_wiki['Wikipedia_MAVG30'])
    top.legend()
    # plt.gcf().set_size_inches(8, 8)
    plt.title('Wikipedia Bitcoin Article Retrievals per day and First Differences')
    bottom = plt.subplot2grid((4,4), (3,0), rowspan=1, colspan=4)
    bottom.bar(dt_pd_wiki.index, dt_pd_wiki['Wikipedia_fd'])
    plt.gcf().set_size_inches(15, 8)

    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + "\F_Figs\\")
    plt.savefig('pt_wiki.pdf')
    plt.show()

    print('Plotting Wikipedia Data done')
    # dt_pd_wiki.dtypes.index
    # dt_pd_wiki.dtypes
    # dt_pd_wiki.select_dtypes(include=[np.datetime64])
    # encoding='utf-8-sig'
    # data = data.iloc[::-1]
if __name__ == '__main__':
    main()
else:
    print("Run From Import")