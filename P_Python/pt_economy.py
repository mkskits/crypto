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

    dt_pd_economy = pd.read_pickle('dt_pd_aggregated_ext.pickle')

    # subsetting date range for plot
    # start_date = '1/1/2016'
    # end_date = '1/1/2018'
    # mask = (dt_pd_vol.index > start_date) & (dt_pd_vol.index <= end_date)
    # dt_pd_aggr = dt_pd_vol[mask]

    matplotlib.rcParams.update({'font.size': 16})

    dt_pd_economy.index.name = ''

    dt_pd_economy['price'] = 100 + np.log(dt_pd_economy['price'] / \
                                dt_pd_economy.iloc[0]['price'])

    dt_pd_economy['tweets'] = 100 + np.log(dt_pd_economy['tweets'] / \
                                 dt_pd_economy.iloc[0]['tweets'])

    dt_pd_economy['wikipedia'] = 100 + np.log(dt_pd_economy['wikipedia'] / \
                                dt_pd_economy.iloc[0]['wikipedia'])

    dt_pd_economy['new_transactions'] = 100 + np.log(dt_pd_economy['new_transactions'] / \
                                dt_pd_economy.iloc[0]['new_transactions'])

    dt_pd_economy['new_curr_transacted'] = 100 + np.log(dt_pd_economy['new_curr_transacted'] / \
                                dt_pd_economy.iloc[0]['new_curr_transacted'])


    f, (ax1) = plt.subplots(1, 1, sharex=True, sharey=True)
    ax2 = ax1.twinx()
    ax1.plot(dt_pd_economy[['price']], color='blue', label='Price', alpha = 0.9)
    ax2.plot(dt_pd_economy[['new_transactions']], color='red', label='Transactions', alpha = 0.9, ls = '-')
    ax2.plot(dt_pd_economy[['new_curr_transacted']], color='green', label='Transaction Volume', alpha=0.9, ls='-')
    # ax1.plot(dt_pd_economy[['tweets']], color='green', label='Tweets', alpha = 0.9, ls = '-')
    ax1.plot(dt_pd_economy[['wikipedia']], color='darkslategrey', label='Wikipedia', alpha=0.9, ls = '-')
    # ax1.plot(dt_pd_economy[['new_posts']], color='black', label='New Posts', alpha=0.9)
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))

    # set size of overall figure not needed here
    plt.gcf().set_size_inches(15, 8)
    # auto-format of x-axis labels & rotation
    f.autofmt_xdate()

    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + sl + "F_Figs" + sl)
    f.tight_layout(pad=0.01)
    plt.savefig('pt_economy.pdf')

    # plt.show()

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")