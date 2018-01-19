import os
# import numpy as np
# print('numpy: %s' % np.__version__)
import pandas as pd
print('pandas: %s' % pd.__version__)
from pandas import Series
import datetime as dt
import pickle
import matplotlib
print('matplotlib: %s' % matplotlib.__version__)
import matplotlib.pyplot as plt

print(os.getcwd())

def main():
    print("First Module's Name: {}".format(__name__))

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    dt_pd_xbt_com = pd.read_pickle('dt_pd_xbt_com.pickle')
    dt_pd_google = pd.read_pickle('dt_pd_google_btc_daily.pickle')
    dt_pd_wiki = pd.read_pickle('dt_pd_wiki.pickle')
    dt_pd_bitcoin_talk = pd.read_pickle('dt_pd_bitcoin_talk.pickle')
    # dt_pd_userstats = pd.read_pickle('dt_pd_bitcoin_economy.pickle')
    dt_pd_twitter_bitinfo = pd.read_pickle('dt_pd_twitter_bitinfo.pickle')
    dt_pd_fin = pd.read_pickle('dt_pd_fin.pickle')


    dt_pd_aggr = dt_pd_xbt_com.merge(dt_pd_wiki, left_index=True, right_index=True, how='inner')
    dt_pd_aggr = dt_pd_aggr.merge(dt_pd_google, left_index=True, right_index=True, how='inner')
    dt_pd_aggr = dt_pd_aggr.merge(dt_pd_fin, left_index=True, right_index=True, how='inner')
    # dt_pd_aggr = dt_pd_aggr.merge(dt_pd_bitcoin_talk, left_index=True, right_index=True, how='inner')
    dt_pd_aggr = dt_pd_aggr.merge(dt_pd_twitter_bitinfo, left_index=True, right_index=True, how='inner')

    dt_pd_aggr.index.name = 'date'
    # rename columns (easier handling in R)
    dt_pd_aggr.rename(columns={'price_usd': 'price', 'google_tr_btc' : 'google', 'DXY' : 'dxy',
                               'XAU': 'xau', 'SPX': 'spx', 'MXWO': 'mxwo', 'QCOM': 'qcom', 'TSM': 'tsm', 'AMD': 'amd',
                               'NVDA': 'nvda', 'High.Yield': 'high.yield', 'Global.Govt': 'global.govt',
                               'US.Govt': 'us.govt', 'DXY.vol': 'dxy.vol', 'XAU.vol': 'xau.vol', 'SPX.vol': 'spx.vol',
                               'MXWO.vol': 'mxwo.vol', 'QCOM.vol': 'qcom.vol', 'TSM.vol': 'tsm.vol',
                               'AMD.vol': 'amd.vol', 'NVDA.vol': 'nvda.vol', 'High.Yield.vol': 'high.yield.vol',
                               'Global.Govt.vol': 'global.govt.vol', 'US.Govt.vol': 'us.govt.vol'}, inplace=True)

    # drop unused columns
    drop_columns = [
        'segment',
        'DXY.fd',
        'XAU.fd',
        'SPX.fd',
        'MXWO.fd',
        'QCOM.fd',
        'TSM.fd',
        'AMD.fd',
        'NVDA.fd',
        'High.Yield.fd',
        'Global.Govt.fd',
        'US.Govt.fd',
        'DXY.pct',
        'XAU.pct',
        'SPX.pct',
        'MXWO.pct',
        'QCOM.pct',
        'TSM.pct',
        'AMD.pct',
        'NVDA.pct',
        'High.Yield.pct',
        'Global.Govt.pct',
        'US.Govt.pct',
        'log.DXY',
        'log.XAU',
        'log.SPX',
        'log.MXWO',
        'log.QCOM',
        'log.TSM',
        'log.AMD',
        'log.NVDA',
        'log.High.Yield',
        'log.Global.Govt',
        'log.US.Govt',
        'price_usd_fd',
        'price_usd_MAVG30'
    ]
    dt_pd_aggr = dt_pd_aggr.drop(drop_columns, 1)

    # store aggr data as pickle and CSV file
    dt_pd_aggr.to_pickle('dt_pd_aggregated_fin_assets.pickle')
    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + sl + 'D_Data')
    dt_pd_aggr.to_csv('dt_aggregated_fin_assets.csv', sep=',')

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
        main()
else:
        print("Run From Import")