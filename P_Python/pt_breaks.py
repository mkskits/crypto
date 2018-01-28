import os
import numpy as np
print('numpy: %s' % np.__version__)
import matplotlib
print('matplotlib: %s' % matplotlib.__version__)
import matplotlib.pyplot as plt
import pandas as pd
print('pandas: %s' % pd.__version__)
import datetime as dt
import pickle
from matplotlib.ticker import FuncFormatter

print(os.getcwd())

def main():
    print("First Module's Name: {}".format(__name__))

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    dt_pd_xbt_com = pd.read_pickle('dt_pd_xbt_com.pickle')
    dt_pd_xbt_com = dt_pd_xbt_com[dt_pd_xbt_com.price_usd != 0]
    dt_pd_xbt_com['segment'] = 1

    # calculate log returns
    # dt_pd_xbt_com['xbt_log'] = np.log(dt_pd_xbt_com['price_usd'])

    # subsetting date range for plot
    # start_date = '1/1/2016'
    # end_date = '1/1/2018'
    # mask = (dt_pd_vol.index > start_date) & (dt_pd_vol.index <= end_date)
    # dt_pd_aggr = dt_pd_vol[mask]

    matplotlib.rcParams.update({'font.size': 16})

    dt_pd_xbt_com.index.name = ''

    f, (ax1) = plt.subplots(1, 1, sharex=True, sharey=True)
    ax1.plot(dt_pd_xbt_com[['price_usd']], color='blue', label='Price (USD)')
    ax1.legend(loc='upper left')

    plt.axvline('2013-11-5' , color = 'red')
    # plt.axvline('2013-11-4', color='red', alpha = 0.1)
    # plt.axvline('2013-11-6', color='red', alpha = 0.1)

    plt.axvline('2017-1-1', color='red')
    # plt.axvline('2017-1-6', color='red', alpha = 0.1)
    # plt.axvline('2016-12-26', color='red', alpha = 0.1)

    plt.axvline('2017-7-4', color='red')
    # plt.axvline('2017-7-9', color='red', alpha = 0.1)
    # plt.axvline('2017-6-30', color='red', alpha=0.1)



    # ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))

    # set size of overall figure not needed here
    plt.gcf().set_size_inches(15, 8)
    # auto-format of x-axis labels & rotation
    f.autofmt_xdate()

    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + sl + "F_Figs" + sl)
    f.tight_layout(pad=0.01)
    plt.savefig('pt_breaks.pdf')

    # plt.show()

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")