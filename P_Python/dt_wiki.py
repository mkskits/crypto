import os
import scipy
print('scipy: %s' % scipy.__version__)
import numpy as np
print('numpy: %s' % np.__version__)
import matplotlib
print('matplotlib: %s' % matplotlib.__version__)
import pandas as pd
print('pandas: %s' % pd.__version__)
import sklearn
import statsmodels
from pandas import Series

print("This will always be run")

def main():
    print("First Module's Name: {}".format(__name__))
    os.chdir('..')

    ## INPUT
    ## Name of Data File (WIKIPEDIA)
    dt_csv_wiki = 'pageviews-20150701-20171025.csv'

    dt_pd_wiki = pd.read_csv(os.path.abspath(os.curdir) + "\D_Data\W_Wikipedia\\" + dt_csv_wiki)
    print(dt_pd_wiki)
    # dt_pd_wiki.select_dtypes(include=[np.datetime64])

    # data.set_index("date", inplace=True)
    #  encoding='utf-8-sig'

    # data = data.iloc[::-1]
    # data.index = pd.to_datetime(data.index)
    # plt.figure(1)
    # plt.subplot(211)
    # plt.plot(data2['date', 'price_usd'])
    # plt.plot(data)
    # data.plot()
    # plt.show()
    # print(data.head())
    # print(list(data))
    #
    # data2 = pd.read_csv(os.path.abspath(os.curdir) + "\D_Data\B_Bloomberg\XBT_clean.csv", encoding='utf-8-sig')
    # data2.set_index("date", inplace=True)
    # data2 = data2.iloc[::-1]
    #
    # print(data2.head())
    # print(list(data2))


if __name__ == '__main__':
    main()
else:
    print("Run From Import")


