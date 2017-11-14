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
from tkinter import Tk
import scipy
# print('scipy: %s' % scipy.__version__)
import numpy as np
# print('numpy: %s' % np.__version__)
# import matplotlib
# print('matplotlib: %s' % matplotlib.__version__)
# import matplotlib.pyplot as plt
import pandas as pd
# print('pandas: %s' % pd.__version__)
# import sklearn
# # import statsmodels
# from pandas import Series
# import datetime as dt
# import pickle
# import pylab

print(os.getcwd())

def main():
    print("First Module's Name: {}".format(__name__))

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    os.chdir('C:\wiki')

    files = ['pagecounts-20100701-000000.gz',
             ]

    for x in files:
        f = gzip.open(x, 'rb')
        file_content = f.read()
        # print(file_content)
        wframe = pd.read_table(gzip.open(x), sep=' ', usecols=[0, 1, 2], names=['project', 'page_title', 'counter'], index_col=['page_title'])


    # r = Tk()
    # r.withdraw()
    # r.clipboard_clear()
    # r.clipboard_append(file_content)
    # r.update()  # now it stays on the clipboard after the window is closed
    # r.destroy()

    print('done')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")