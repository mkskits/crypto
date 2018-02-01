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

    dt_fin = pd.read_pickle('dt_pd_fin.pickle')

    # subsetting date range for plot
    # start_date = '1/1/2016'
    # end_date = '1/1/2018'
    # mask = (dt_pd_vol.index > start_date) & (dt_pd_vol.index <= end_date)
    # dt_pd_aggr = dt_pd_vol[mask]

    matplotlib.rcParams.update({'font.size': 16})

    dt_fin.index.name = ''

    dt_fin['DXY'] = 100 * dt_fin['DXY'] / \
                                dt_fin.iloc[0]['DXY']

    dt_fin['XAU'] = 100 * dt_fin['XAU'] / \
                                 dt_fin.iloc[0]['XAU']

    dt_fin['SPX'] = 100 * dt_fin['SPX'] / \
                                 dt_fin.iloc[0]['SPX']

    dt_fin['NVDA'] = 100 * dt_fin['NVDA'] / \
                                 dt_fin.iloc[0]['NVDA']

    dt_fin['QCOM'] = 100 * dt_fin['QCOM'] / \
                                dt_fin.iloc[0]['QCOM']

    dt_fin['TSM'] = 100 * dt_fin['TSM'] / \
                                dt_fin.iloc[0]['TSM']

    dt_fin['AMD'] = 100 * dt_fin['AMD'] / \
                                     dt_fin.iloc[0]['AMD']

    dt_fin['High.Yield'] = 100 * dt_fin['High.Yield'] / \
                                    dt_fin.iloc[0]['High.Yield']

    dt_fin['Global.Govt'] = 100 * dt_fin['Global.Govt'] / \
                                     dt_fin.iloc[0]['Global.Govt']

    dt_fin['US.Govt'] = 100 * dt_fin['US.Govt'] / \
                            dt_fin.iloc[0]['US.Govt']

    f, (ax1) = plt.subplots(1, 1, sharex=True, sharey=True)
    ax2 = ax1.twinx()
    ax1.plot(dt_fin[['XAU']], label='XAU')
    ax1.plot(dt_fin[['DXY']], label='DXY')
    ax1.plot(dt_fin[['SPX']],  label='SPX')
    ax2.plot(dt_fin[['NVDA']], label='NVDA', color = 'purple')
    ax1.plot(dt_fin[['QCOM']], label='QCOM')
    ax1.plot(dt_fin[['TSM']],  label='TSM')
    ax1.plot(dt_fin[['AMD']], label='AMD')
    ax1.plot(dt_fin[['High.Yield']], label='High Yield')
    ax1.plot(dt_fin[['Global.Govt']], label='Global Govt')
    ax1.plot(dt_fin[['US.Govt']], label='US Govt')
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
    plt.savefig('pt_financial.pdf')

    # plt.show()

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")