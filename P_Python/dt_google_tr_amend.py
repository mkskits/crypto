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
import pytrends
import lxml
from pytrends.request import TrendReq

print(os.getcwd())

def main():
    print("First Module's Name: {}".format(__name__))
    print('OS:', os.name)
    os.chdir('..')

dt_pd_google = pd.read_pickle('dt_pd_google.pickle')

dt_pd_google.rename(columns={'Bitcoin': 'google_tr'}, inplace=True)

plt.plot(dt_pd_google['Bitcoin'])
plt.show()

print('google script amendment done')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")