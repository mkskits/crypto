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

print(os.getcwd())

def main():
    print("First Module's Name: {}".format(__name__))

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    # All Files to be read in current cycle of scraping
    files = []
    with open('config.ini') as f:
        files = f.read().splitlines()
        f.close()

    # md5 checksum hashes to python
    dt_md5 = 'md5sums.txt'
    dt_pd_md5 = pd.read_table(os.path.dirname(os.path.realpath(__file__)) + sl + dt_md5, delim_whitespace=True,
                              header=None, names=['md5', 'fname'], index_col=1)
    t = 0
    for x in files:
        if hashlib.md5(open(x, 'rb').read()).hexdigest() == dt_pd_md5.loc[x]['md5']:
            print('md5 match', x)
        else:
            print('md5 error in', x)

    # dt_pd_wiki_legacy['tstamp'] = pd.to_datetime(dt_pd_wiki_legacy['tstamp'])

    print('md5 check done')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")