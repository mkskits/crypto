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
import io
import time

print(os.getcwd())

def main():
    print(time.strftime("%H:%M:%S"))
    print("First Module's Name: {}".format(__name__))

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    # All Files to be read in current cycle of scraping
    files = [
        'pagecounts-20130201-170000.gz'
    ]

    # md5 checksum hashes to python
    dt_md5 = 'md5sums.txt'
    dt_pd_md5 = pd.read_table(os.path.dirname(os.path.realpath(__file__)) + sl + dt_md5, delim_whitespace=True,
                              header=None, names=['md5', 'fname'], index_col=1, dtype={'md5': str, 'fname': str})

    dt_pd_wiki_legacy = pd.DataFrame(columns=['project', 'page_title', 'counter', 'rsize', 'tstamp'])
    dt_pd_wiki_legacy.set_index('page_title', inplace=True, drop=True, append=False, verify_integrity=True)

    t = 0

    wframe = pd.DataFrame(
                   columns=['project', 'page_title', 'counter', 'rsize'], index=['page_title'],
                   # warn_bad_lines=True,
                   # dtype={'project': str, 'page_title': str, 'counter': int, 'rsize': float},
                   # error_bad_lines=False,
                   )
    temp = []

    for x in files:
        if hashlib.md5(open(x, 'rb').read()).hexdigest() == dt_pd_md5.loc[x]['md5']:
            print('md5 match', x)
            try:
                print('we are here')
                f = gzip.open(x, 'rb')
                for line in f:
                    if len(line) < 26:
                        temp.append(line)
            except Exception:
                pass

    print('test')
    print('test')

            #     for line in f.readlines():
            #         if len(line) < 26:
            #             try:
            #                 winp = io.StringIO(line.decode('utf-8', errors='replace'), newline='\n')
            #                 wframe = pd.read_table(winp, sep=' ', usecols=[0, 1, 2, 3],
            #                                names=['project', 'page_title', 'counter', 'rsize'], index_col=['page_title'],
            #                                warn_bad_lines=True,
            #                                dtype={'project': str, 'page_title': str, 'counter': int, 'rsize': float},
            #                                error_bad_lines=False,
            #                                )
            #                 try:
            #                     wframe = wframe.loc['Bitcoin']
            #                     wframe['tstamp'] = x[11:-3]
            #                     dt_pd_wiki_legacy = dt_pd_wiki_legacy.append(wframe)
            #                     dt_pd_wiki_legacy['tstamp'] = pd.to_datetime(dt_pd_wiki_legacy['tstamp'])
            #                     print('----------------------------')
            #                     print(t)
            #                     print('progres: ', round((t / len(files))*100, 1), "%")
            #                     dt_pd_wiki_legacy.to_pickle('dt_pd_wiki_legacy.pickle')
            #                     t = t + 1
            #                 except Exception:
            #                     pass
            #             except Exception:
            #                 pass
            #     f.close()
            # except Exception:
            #     raise
            #     # print('gzip open error in ', x)


    # dt_pd_wiki_legacy['tstamp'] = pd.to_datetime(dt_pd_wiki_legacy['tstamp'])
    print(time.strftime("%H:%M:%S"))
    print('current cycle of scraping done')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")