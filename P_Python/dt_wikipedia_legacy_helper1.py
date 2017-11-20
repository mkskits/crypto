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
print('pandas: %s' % pd.__version__)

print(os.getcwd())

def main():
    print("First Module's Name: {}".format(__name__))

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    check = pd.read_pickle('dt_pd_wiki_legacy_2010-07.pickle')

    print('current cycle of scraping done')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")