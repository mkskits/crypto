# https://pypi.python.org/pypi/mwviews
# https://github.com/Commonists/pageview-api
# https://wikimedia.org/api/rest_v1/#!/Pageviews_data/get_metrics_pageviews_per_article_project_access_agent_article_granularity_start_end
# actual (not legacy) https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/all-agents/bitcoin/daily/2010071800/20181124

# https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/all-agents/bitcoin/daily/2010071800/20181124
# https://wikitech.wikimedia.org/wiki/Analytics/Pageviews
# https://wikitech.wikimedia.org/wiki/Analytics/Systems/Dashiki
# https://github.com/abelsson/stats.grok.se/blob/master/backend/getstats.py
# https://dumps.wikimedia.org/other/pagecounts-raw/
# https://dumps.wikimedia.org/other/pagecounts-ez/

import gzip
import os
# from tkinter import Tk
import scipy
import datetime as dt
print('scipy: %s' % scipy.__version__)
import numpy as np
print('numpy: %s' % np.__version__)
import pandas as pd
import hashlib
print('pandas: %s' % pd.__version__)
# import matplotlib
# print('matplotlib: %s' % matplotlib.__version__)
# import matplotlib.pyplot as plt
# import sklearn
# # import statsmodels
# from pandas import Series
# import pickle
# import pylab

print(os.getcwd())

def main():
    print("First Module's Name: {}".format(__name__))

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    c1 = pd.read_pickle('dt_pd_wiki_legacy_2014-07a.pickle')
    c2 = pd.read_pickle('dt_pd_wiki_legacy_2014-07b.pickle')
    c1c = pd.DataFrame(columns=['tstamp'])

    # z=0
    # for x in c1['tstamp']:
    #     # print(x)
    #     try:
    #         x = pd.to_datetime(x)
    #         c1['tstamp'].iloc[z] = x
    #         z = z + 1
    #         # c1c = c1c.append({'tstamp':x}, ignore_index=True)
    #     except Exception:
    #         print('error in: ', x)

    c1 = c1.append(c2)
    c1.to_pickle('dt_pd_wiki_legacy_2014-07.pickle')

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")