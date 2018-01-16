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
    dt_pd_xbt_com['xbt_log_ret'] = np.log(dt_pd_xbt_com['price_usd'] / dt_pd_xbt_com['price_usd'].shift(1))

    # calculate annualized volatility based on 30day rolling window
    dt_pd_xbt_com['XBT.vol'] = dt_pd_xbt_com['xbt_log_ret'].rolling(window=30, center=False).std() * np.sqrt(365)
    dt_pd_xbt_com = dt_pd_xbt_com['XBT.vol']
    dt_pd_xbt_com = dt_pd_xbt_com.to_frame()

    dt_pd_fin = pd.read_pickle('dt_pd_fin.pickle')
    dt_pd_fin = dt_pd_fin[['DXY.vol', 'XAU.vol', 'SPX.vol']]

    dt_pd_vol = dt_pd_xbt_com.merge(dt_pd_fin, left_index=True, right_index=True, how='inner')
    dt_pd_vol.dropna(axis=0, how='any', inplace=True)

    # subsetting date range for plot
    # start_date = '1/1/2016'
    # end_date = '1/1/2018'
    # mask = (dt_pd_vol.index > start_date) & (dt_pd_vol.index <= end_date)
    # dt_pd_aggr = dt_pd_vol[mask]

    matplotlib.rcParams.update({'font.size': 16})

    dt_pd_vol.index.name = ''

    f, (ax1) = plt.subplots(1, 1, sharex=True, sharey=True)
    ax1.plot(dt_pd_vol[['XBT.vol']], color='blue', label='$\sigma_{Bitcoin}$')
    ax1.plot(dt_pd_vol[['XAU.vol']], color='red', label='$\sigma_{Gold}$')
    ax1.plot(dt_pd_vol[['SPX.vol']], color='green', label='$\sigma_{S&P\,500}$')
    ax1.legend(loc='upper right')

    ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))

    # set size of overall figure not needed here
    plt.gcf().set_size_inches(15, 8)
    # auto-format of x-axis labels & rotation
    f.autofmt_xdate()

    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + sl + "F_Figs" + sl)
    f.tight_layout(pad=0.01)
    plt.savefig('pt_hist_volatility.pdf')

    # plt.show()

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")