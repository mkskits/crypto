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
    dt_pd_xbt_com['xbt_vol_30d_ann'] = dt_pd_xbt_com['xbt_log_ret'].rolling(window=30, center=False).std() * np.sqrt(365)
    dt_pd_xbt_com = dt_pd_xbt_com['xbt_vol_30d_ann']
    dt_pd_xbt_com = dt_pd_xbt_com.to_frame()
    # dt_pd_xbt_com.set_index('date', inplace=True, drop=True, append=False, verify_integrity=False)

    dt_pd_fin = pd.read_pickle('dt_pd_fin.pickle')
    dt_pd_fin = dt_pd_fin[['DXY.vol', 'XAU.vol', 'SPX.vol']]
    # dt_pd_fin.set_index('date', inplace=True, drop=True, append=False, verify_integrity=False)

    dt_pd_vol = dt_pd_xbt_com.merge(dt_pd_fin, left_index=True, right_index=True, how='inner')
    dt_pd_vol.dropna(axis=0, how='any', inplace=True)
    dt_pd_vol.rename(columns={'xbt_vol_30d_ann': 'XBT.vol'}, inplace=True)

    # subsetting date range for plot
    # start_date = '1/1/2016'
    # end_date = '1/1/2018'
    # mask = (dt_pd_aggr.index > start_date) & (dt_pd_aggr.index <= end_date)
    # dt_pd_aggr = dt_pd_aggr[mask]

    def make_patch_spines_invisible(ax):
        ax.set_frame_on(True)
        ax.patch.set_visible(False)
        for sp in ax.spines.values():
            sp.set_visible(False)

    matplotlib.rcParams.update({'font.size': 16})

    fig = plt.figure()

    fig, host = plt.subplots()
    fig.subplots_adjust(right=0.75)

    par1 = host.twinx()
    par2 = host.twinx()

    # Offset the right spine of par2.  The ticks and label have already been
    # placed on the right by twinx above.
    par2.spines["right"].set_position(("axes", 1.2))
    # Having been created by twinx, par2 has its frame off, so the line of its
    # detached spine is invisible.  First, activate the frame but make the patch
    # and spines invisible.
    make_patch_spines_invisible(par2)
    # Second, show the right spine.
    par2.spines["right"].set_visible(True)

    # p1, = host.plot(dt_pd_aggr.index, dt_pd_aggr['price_usd'], "b-", label="Price_USD")
    p1, = host.plot(dt_pd_vol.index, dt_pd_vol['XBT.vol'], "b-", label="Bitcoin")
    p2, = par1.plot(dt_pd_vol.index, dt_pd_vol['XAU.vol'], "r-", label="Gold")
    p3, = par2.plot(dt_pd_vol.index, dt_pd_vol['SPX.vol'], "g-", label="S&P500")

    # host.set_xlim(0, 2)
    # host.set_ylim(0, 2)
    # par1.set_ylim(0, 4)
    # par2.set_ylim(1, 65)

    host.set_xlabel('')
    #host.set_ylabel('Price (USD)')
    #par1.set_ylabel('Wikipedia')
    #par2.set_ylabel('Google Trend')

    host.yaxis.label.set_color(p1.get_color())
    par1.yaxis.label.set_color(p2.get_color())
    par2.yaxis.label.set_color(p3.get_color())

    tkw = dict(size=4, width=1.5)
    host.tick_params(axis='y', colors=p1.get_color(), **tkw)
    par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
    par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
    host.tick_params(axis='x', **tkw)

    lines = [p1, p2, p3]

    host.legend(lines, [l.get_label() for l in lines], loc='best')

    # ax1.plot(dt_pd_aggr.index, dt_pd_aggr['price_usd'],)
    # top.plot(dt_pd_aggr.index, dt_pd_aggr['google_tr'f])
    # top.plot(dt_pd_aggr.index, dt_pd_aggr['wikipedia'])

    # top.legend(loc='best')
    # no title, provided in TeX environment
    # plt.title('Social and Economic Time Series')
    plt.gcf().set_size_inches(15, 8)

    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + sl + "F_Figs" + sl)
    plt.tight_layout(pad=1.8)
    plt.savefig('pt_hist_volatility.pdf') # bbox_inches='tight'

    # plt.show()

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")