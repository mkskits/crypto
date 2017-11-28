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
        'pagecounts-20130301-000000.gz',
        'pagecounts-20130301-010000.gz',
        'pagecounts-20130301-020000.gz',
        'pagecounts-20130301-030000.gz',
        'pagecounts-20130301-040000.gz',
        'pagecounts-20130301-050000.gz',
        'pagecounts-20130301-060000.gz',
        'pagecounts-20130301-070000.gz',
        'pagecounts-20130301-080000.gz',
        'pagecounts-20130301-090001.gz',
        'pagecounts-20130301-100000.gz',
        'pagecounts-20130301-110000.gz',
        'pagecounts-20130301-120000.gz',
        'pagecounts-20130301-130000.gz',
        'pagecounts-20130301-140000.gz',
        'pagecounts-20130301-150000.gz',
        'pagecounts-20130301-160000.gz',
        'pagecounts-20130301-170000.gz',
        'pagecounts-20130301-180000.gz',
        'pagecounts-20130301-190000.gz',
        'pagecounts-20130301-200001.gz',
        'pagecounts-20130301-210000.gz',
        'pagecounts-20130301-220000.gz',
        'pagecounts-20130301-230000.gz',
        'pagecounts-20130302-000000.gz',
        'pagecounts-20130302-010000.gz',
        'pagecounts-20130302-020000.gz',
        'pagecounts-20130302-030000.gz',
        'pagecounts-20130302-040000.gz',
        'pagecounts-20130302-050000.gz',
        'pagecounts-20130302-060000.gz',
        'pagecounts-20130302-070000.gz',
        'pagecounts-20130302-080001.gz',
        'pagecounts-20130302-090000.gz',
        'pagecounts-20130302-100000.gz',
        'pagecounts-20130302-110000.gz',
        'pagecounts-20130302-120000.gz',
        'pagecounts-20130302-130000.gz',
        'pagecounts-20130302-140000.gz',
        'pagecounts-20130302-150000.gz',
        'pagecounts-20130302-160000.gz',
        'pagecounts-20130302-170000.gz',
        'pagecounts-20130302-180000.gz',
        'pagecounts-20130302-190000.gz',
        'pagecounts-20130302-200001.gz',
        'pagecounts-20130302-210000.gz',
        'pagecounts-20130302-220000.gz',
        'pagecounts-20130302-230000.gz',
        'pagecounts-20130303-000000.gz',
        'pagecounts-20130303-010000.gz',
        'pagecounts-20130303-020000.gz',
        'pagecounts-20130303-030000.gz',
        'pagecounts-20130303-040000.gz',
        'pagecounts-20130303-050000.gz',
        'pagecounts-20130303-060000.gz',
        'pagecounts-20130303-070001.gz',
        'pagecounts-20130303-080000.gz',
        'pagecounts-20130303-090000.gz',
        'pagecounts-20130303-100000.gz',
        'pagecounts-20130303-110000.gz',
        'pagecounts-20130303-120000.gz',
        'pagecounts-20130303-130000.gz',
        'pagecounts-20130303-140000.gz',
        'pagecounts-20130303-150000.gz',
        'pagecounts-20130303-160000.gz',
        'pagecounts-20130303-170000.gz',
        'pagecounts-20130303-180000.gz',
        'pagecounts-20130303-190001.gz',
        'pagecounts-20130303-200000.gz',
        'pagecounts-20130303-210000.gz',
        'pagecounts-20130303-220000.gz',
        'pagecounts-20130303-230000.gz',
        'pagecounts-20130304-000000.gz',
        'pagecounts-20130304-010000.gz',
        'pagecounts-20130304-020000.gz',
        'pagecounts-20130304-030000.gz',
        'pagecounts-20130304-040000.gz',
        'pagecounts-20130304-050001.gz',
        'pagecounts-20130304-060000.gz',
        'pagecounts-20130304-070000.gz',
        'pagecounts-20130304-080000.gz',
        'pagecounts-20130304-090000.gz',
        'pagecounts-20130304-100000.gz',
        'pagecounts-20130304-110000.gz',
        'pagecounts-20130304-120000.gz',
        'pagecounts-20130304-130000.gz',
        'pagecounts-20130304-140000.gz',
        'pagecounts-20130304-150000.gz',
        'pagecounts-20130304-160000.gz',
        'pagecounts-20130304-170001.gz',
        'pagecounts-20130304-180000.gz',
        'pagecounts-20130304-190000.gz',
        'pagecounts-20130304-200000.gz',
        'pagecounts-20130304-210000.gz',
        'pagecounts-20130304-220000.gz',
        'pagecounts-20130304-230000.gz',
        'pagecounts-20130305-000000.gz',
        'pagecounts-20130305-010000.gz',
        'pagecounts-20130305-020000.gz',
        'pagecounts-20130305-030000.gz',
        'pagecounts-20130305-040001.gz',
        'pagecounts-20130305-050000.gz',
        'pagecounts-20130305-060000.gz',
        'pagecounts-20130305-070000.gz',
        'pagecounts-20130305-080000.gz',
        'pagecounts-20130305-090000.gz',
        'pagecounts-20130305-100000.gz',
        'pagecounts-20130305-110000.gz',
        'pagecounts-20130305-120000.gz',
        'pagecounts-20130305-130000.gz',
        'pagecounts-20130305-140000.gz',
        'pagecounts-20130305-150001.gz',
        'pagecounts-20130305-160000.gz',
        'pagecounts-20130305-170000.gz',
        'pagecounts-20130305-180000.gz',
        'pagecounts-20130305-190000.gz',
        'pagecounts-20130305-200000.gz',
        'pagecounts-20130305-210000.gz',
        'pagecounts-20130305-220000.gz',
        'pagecounts-20130305-230000.gz',
        'pagecounts-20130306-000000.gz',
        'pagecounts-20130306-010000.gz',
        'pagecounts-20130306-020001.gz',
        'pagecounts-20130306-030000.gz',
        'pagecounts-20130306-040000.gz',
        'pagecounts-20130306-050000.gz',
        'pagecounts-20130306-060000.gz',
        'pagecounts-20130306-070000.gz',
        'pagecounts-20130306-080000.gz',
        'pagecounts-20130306-090000.gz',
        'pagecounts-20130306-100000.gz',
        'pagecounts-20130306-110000.gz',
        'pagecounts-20130306-120000.gz',
        'pagecounts-20130306-130001.gz',
        'pagecounts-20130306-140000.gz',
        'pagecounts-20130306-150000.gz',
        'pagecounts-20130306-160000.gz',
        'pagecounts-20130306-170000.gz',
        'pagecounts-20130306-180000.gz',
        'pagecounts-20130306-190000.gz',
        'pagecounts-20130306-200000.gz',
        'pagecounts-20130306-210000.gz',
        'pagecounts-20130306-220000.gz',
        'pagecounts-20130306-230000.gz',
        'pagecounts-20130307-000001.gz',
        'pagecounts-20130307-010000.gz',
        'pagecounts-20130307-020000.gz',
        'pagecounts-20130307-030000.gz',
        'pagecounts-20130307-040000.gz',
        'pagecounts-20130307-050000.gz',
        'pagecounts-20130307-060000.gz',
        'pagecounts-20130307-070000.gz',
        'pagecounts-20130307-080000.gz',
        'pagecounts-20130307-090000.gz',
        'pagecounts-20130307-100000.gz',
        'pagecounts-20130307-110000.gz',
        'pagecounts-20130307-120001.gz',
        'pagecounts-20130307-130000.gz',
        'pagecounts-20130307-140000.gz',
        'pagecounts-20130307-150000.gz',
        'pagecounts-20130307-160000.gz',
        'pagecounts-20130307-170000.gz',
        'pagecounts-20130307-180000.gz',
        'pagecounts-20130307-190000.gz',
        'pagecounts-20130307-200000.gz',
        'pagecounts-20130307-210000.gz',
        'pagecounts-20130307-220000.gz',
        'pagecounts-20130307-230001.gz',
        'pagecounts-20130308-000000.gz',
        'pagecounts-20130308-010000.gz',
        'pagecounts-20130308-020000.gz',
        'pagecounts-20130308-030000.gz',
        'pagecounts-20130308-040000.gz',
        'pagecounts-20130308-050000.gz',
        'pagecounts-20130308-060000.gz',
        'pagecounts-20130308-070000.gz',
        'pagecounts-20130308-080000.gz',
        'pagecounts-20130308-090000.gz',
        'pagecounts-20130308-100000.gz',
        'pagecounts-20130308-110001.gz',
        'pagecounts-20130308-120000.gz',
        'pagecounts-20130308-130000.gz',
        'pagecounts-20130308-140000.gz',
        'pagecounts-20130308-150000.gz',
        'pagecounts-20130308-160000.gz',
        'pagecounts-20130308-170000.gz',
        'pagecounts-20130308-180000.gz',
        'pagecounts-20130308-190000.gz',
        'pagecounts-20130308-200000.gz',
        'pagecounts-20130308-210000.gz',
        'pagecounts-20130308-220001.gz',
        'pagecounts-20130308-230000.gz',
        'pagecounts-20130309-000000.gz',
        'pagecounts-20130309-010000.gz',
        'pagecounts-20130309-020000.gz',
        'pagecounts-20130309-030000.gz',
        'pagecounts-20130309-040000.gz',
        'pagecounts-20130309-050000.gz',
        'pagecounts-20130309-060000.gz',
        'pagecounts-20130309-070000.gz',
        'pagecounts-20130309-080000.gz',
        'pagecounts-20130309-090001.gz',
        'pagecounts-20130309-100000.gz',
        'pagecounts-20130309-110000.gz',
        'pagecounts-20130309-120000.gz',
        'pagecounts-20130309-130000.gz',
        'pagecounts-20130309-140000.gz',
        'pagecounts-20130309-150000.gz',
        'pagecounts-20130309-160000.gz',
        'pagecounts-20130309-170000.gz',
        'pagecounts-20130309-180000.gz',
        'pagecounts-20130309-190000.gz',
        'pagecounts-20130309-200001.gz',
        'pagecounts-20130309-210000.gz',
        'pagecounts-20130309-220000.gz',
        'pagecounts-20130309-230000.gz',
        'pagecounts-20130310-000000.gz',
        'pagecounts-20130310-010000.gz',
        'pagecounts-20130310-020000.gz',
        'pagecounts-20130310-030000.gz',
        'pagecounts-20130310-040000.gz',
        'pagecounts-20130310-050000.gz',
        'pagecounts-20130310-060000.gz',
        'pagecounts-20130310-070000.gz',
        'pagecounts-20130310-080001.gz',
        'pagecounts-20130310-090000.gz',
        'pagecounts-20130310-100000.gz',
        'pagecounts-20130310-110000.gz',
        'pagecounts-20130310-120000.gz',
        'pagecounts-20130310-130000.gz',
        'pagecounts-20130310-140000.gz',
        'pagecounts-20130310-150000.gz',
        'pagecounts-20130310-160000.gz',
        'pagecounts-20130310-170000.gz',
        'pagecounts-20130310-180000.gz',
        'pagecounts-20130310-190001.gz',
        'pagecounts-20130310-200000.gz',
        'pagecounts-20130310-210000.gz',
        'pagecounts-20130310-220000.gz',
        'pagecounts-20130310-230000.gz',
        'pagecounts-20130311-000000.gz',
        'pagecounts-20130311-010000.gz',
        'pagecounts-20130311-020000.gz',
        'pagecounts-20130311-030000.gz',
        'pagecounts-20130311-040000.gz',
        'pagecounts-20130311-050000.gz',
        'pagecounts-20130311-060001.gz',
        'pagecounts-20130311-070000.gz',
        'pagecounts-20130311-080000.gz',
        'pagecounts-20130311-090000.gz',
        'pagecounts-20130311-100000.gz',
        'pagecounts-20130311-110000.gz',
        'pagecounts-20130311-120000.gz',
        'pagecounts-20130311-130000.gz',
        'pagecounts-20130311-140000.gz',
        'pagecounts-20130311-150000.gz',
        'pagecounts-20130311-160000.gz',
        'pagecounts-20130311-170001.gz',
        'pagecounts-20130311-180000.gz',
        'pagecounts-20130311-190000.gz',
        'pagecounts-20130311-200000.gz',
        'pagecounts-20130311-210000.gz',
        'pagecounts-20130311-220000.gz',
        'pagecounts-20130311-230000.gz',
        'pagecounts-20130312-000000.gz',
        'pagecounts-20130312-010000.gz',
        'pagecounts-20130312-020000.gz',
        'pagecounts-20130312-030001.gz',
        'pagecounts-20130312-040000.gz',
        'pagecounts-20130312-050000.gz',
        'pagecounts-20130312-060000.gz',
        'pagecounts-20130312-070000.gz',
        'pagecounts-20130312-080000.gz',
        'pagecounts-20130312-090000.gz',
        'pagecounts-20130312-100000.gz',
        'pagecounts-20130312-110000.gz',
        'pagecounts-20130312-120000.gz',
        'pagecounts-20130312-130000.gz',
        'pagecounts-20130312-140000.gz',
        'pagecounts-20130312-150001.gz',
        'pagecounts-20130312-160000.gz',
        'pagecounts-20130312-170000.gz',
        'pagecounts-20130312-180000.gz',
        'pagecounts-20130312-190000.gz',
        'pagecounts-20130312-200000.gz',
        'pagecounts-20130312-210000.gz',
        'pagecounts-20130312-220000.gz',
        'pagecounts-20130312-230000.gz',
        'pagecounts-20130313-000000.gz',
        'pagecounts-20130313-010001.gz',
        'pagecounts-20130313-020000.gz',
        'pagecounts-20130313-030000.gz',
        'pagecounts-20130313-040000.gz',
        'pagecounts-20130313-050000.gz',
        'pagecounts-20130313-060000.gz',
        'pagecounts-20130313-070000.gz',
        'pagecounts-20130313-080000.gz',
        'pagecounts-20130313-090000.gz',
        'pagecounts-20130313-100000.gz',
        'pagecounts-20130313-110000.gz',
        'pagecounts-20130313-120000.gz',
        'pagecounts-20130313-130001.gz',
        'pagecounts-20130313-140000.gz',
        'pagecounts-20130313-150000.gz',
        'pagecounts-20130313-160000.gz',
        'pagecounts-20130313-170000.gz',
        'pagecounts-20130313-180000.gz',
        'pagecounts-20130313-190000.gz',
        'pagecounts-20130313-200001.gz',
        'pagecounts-20130313-210000.gz',
        'pagecounts-20130313-220000.gz',
        'pagecounts-20130313-230000.gz',
        'pagecounts-20130314-000000.gz',
        'pagecounts-20130314-010000.gz',
        'pagecounts-20130314-020000.gz',
        'pagecounts-20130314-030001.gz',
        'pagecounts-20130314-040000.gz',
        'pagecounts-20130314-050000.gz',
        'pagecounts-20130314-060000.gz',
        'pagecounts-20130314-070000.gz',
        'pagecounts-20130314-080000.gz',
        'pagecounts-20130314-090000.gz',
        'pagecounts-20130314-100000.gz',
        'pagecounts-20130314-110000.gz',
        'pagecounts-20130314-120000.gz',
        'pagecounts-20130314-130000.gz',
        'pagecounts-20130314-140000.gz',
        'pagecounts-20130314-150001.gz',
        'pagecounts-20130314-160000.gz',
        'pagecounts-20130314-170000.gz',
        'pagecounts-20130314-180000.gz',
        'pagecounts-20130314-190000.gz',
        'pagecounts-20130314-200000.gz',
        'pagecounts-20130314-210000.gz',
        'pagecounts-20130314-220000.gz',
        'pagecounts-20130314-230000.gz',
        'pagecounts-20130315-000000.gz',
        'pagecounts-20130315-010000.gz',
        'pagecounts-20130315-020001.gz',
        'pagecounts-20130315-030000.gz',
        'pagecounts-20130315-040000.gz',
        'pagecounts-20130315-050000.gz',
        'pagecounts-20130315-060000.gz',
        'pagecounts-20130315-070000.gz',
        'pagecounts-20130315-080000.gz',
        'pagecounts-20130315-090000.gz',
        'pagecounts-20130315-100000.gz',
        'pagecounts-20130315-110000.gz',
        'pagecounts-20130315-120000.gz',
        'pagecounts-20130315-130000.gz',
        'pagecounts-20130315-140001.gz',
        'pagecounts-20130315-150000.gz',
        'pagecounts-20130315-160000.gz',
        'pagecounts-20130315-170000.gz',
        'pagecounts-20130315-180000.gz',
        'pagecounts-20130315-190000.gz',
        'pagecounts-20130315-200000.gz',
        'pagecounts-20130315-210000.gz',
        'pagecounts-20130315-220000.gz',
        'pagecounts-20130315-230000.gz',
        'pagecounts-20130316-000000.gz',
        'pagecounts-20130316-010001.gz',
        'pagecounts-20130316-020000.gz',
        'pagecounts-20130316-030000.gz',
        'pagecounts-20130316-040000.gz',
        'pagecounts-20130316-050000.gz',
        'pagecounts-20130316-060000.gz',
        'pagecounts-20130316-070000.gz',
        'pagecounts-20130316-080000.gz',
        'pagecounts-20130316-090000.gz',
        'pagecounts-20130316-100000.gz',
        'pagecounts-20130316-110000.gz',
        'pagecounts-20130316-120000.gz',
        'pagecounts-20130316-130001.gz',
        'pagecounts-20130316-140000.gz',
        'pagecounts-20130316-150000.gz',
        'pagecounts-20130316-160000.gz',
        'pagecounts-20130316-170000.gz',
        'pagecounts-20130316-180000.gz',
        'pagecounts-20130316-190000.gz',
        'pagecounts-20130316-200000.gz',
        'pagecounts-20130316-210000.gz',
        'pagecounts-20130316-220000.gz',
        'pagecounts-20130316-230000.gz',
        'pagecounts-20130317-000000.gz',
        'pagecounts-20130317-010001.gz',
        'pagecounts-20130317-020000.gz',
        'pagecounts-20130317-030000.gz',
        'pagecounts-20130317-040000.gz',
        'pagecounts-20130317-050000.gz',
        'pagecounts-20130317-060000.gz',
        'pagecounts-20130317-070000.gz',
        'pagecounts-20130317-080000.gz',
        'pagecounts-20130317-090000.gz',
        'pagecounts-20130317-100000.gz',
        'pagecounts-20130317-110000.gz',
        'pagecounts-20130317-120000.gz',
        'pagecounts-20130317-130001.gz',
        'pagecounts-20130317-140000.gz',
        'pagecounts-20130317-150000.gz',
        'pagecounts-20130317-160000.gz',
        'pagecounts-20130317-170000.gz',
        'pagecounts-20130317-180000.gz',
        'pagecounts-20130317-190000.gz',
        'pagecounts-20130317-200000.gz',
        'pagecounts-20130317-210000.gz',
        'pagecounts-20130317-220000.gz',
        'pagecounts-20130317-230001.gz',
        'pagecounts-20130318-000000.gz',
        'pagecounts-20130318-010000.gz',
        'pagecounts-20130318-020000.gz',
        'pagecounts-20130318-030000.gz',
        'pagecounts-20130318-040000.gz',
        'pagecounts-20130318-050000.gz',
        'pagecounts-20130318-060000.gz',
        'pagecounts-20130318-070000.gz',
        'pagecounts-20130318-080000.gz',
        'pagecounts-20130318-090000.gz',
        'pagecounts-20130318-100000.gz',
        'pagecounts-20130318-110001.gz',
        'pagecounts-20130318-120000.gz',
        'pagecounts-20130318-130000.gz',
        'pagecounts-20130318-140000.gz',
        'pagecounts-20130318-150000.gz',
        'pagecounts-20130318-160000.gz',
        'pagecounts-20130318-170000.gz',
        'pagecounts-20130318-180000.gz',
        'pagecounts-20130318-190000.gz',
        'pagecounts-20130318-200000.gz',
        'pagecounts-20130318-210000.gz',
        'pagecounts-20130318-220001.gz',
        'pagecounts-20130318-230000.gz',
        'pagecounts-20130319-000000.gz',
        'pagecounts-20130319-010000.gz',
        'pagecounts-20130319-020000.gz',
        'pagecounts-20130319-030000.gz',
        'pagecounts-20130319-040000.gz',
        'pagecounts-20130319-050000.gz',
        'pagecounts-20130319-060000.gz',
        'pagecounts-20130319-070000.gz',
        'pagecounts-20130319-080000.gz',
        'pagecounts-20130319-090000.gz',
        'pagecounts-20130319-100001.gz',
        'pagecounts-20130319-110000.gz',
        'pagecounts-20130319-120000.gz',
        'pagecounts-20130319-130000.gz',
        'pagecounts-20130319-140000.gz',
        'pagecounts-20130319-150000.gz',
        'pagecounts-20130319-160000.gz',
        'pagecounts-20130319-170000.gz',
        'pagecounts-20130319-180000.gz',
        'pagecounts-20130319-190000.gz',
        'pagecounts-20130319-200000.gz',
        'pagecounts-20130319-210000.gz',
        'pagecounts-20130319-220001.gz',
        'pagecounts-20130319-230000.gz',
        'pagecounts-20130320-000000.gz',
        'pagecounts-20130320-010000.gz',
        'pagecounts-20130320-020000.gz',
        'pagecounts-20130320-030000.gz',
        'pagecounts-20130320-040000.gz',
        'pagecounts-20130320-050000.gz',
        'pagecounts-20130320-060000.gz',
        'pagecounts-20130320-070000.gz',
        'pagecounts-20130320-080000.gz',
        'pagecounts-20130320-090000.gz',
        'pagecounts-20130320-100001.gz',
        'pagecounts-20130320-110000.gz',
        'pagecounts-20130320-120000.gz',
        'pagecounts-20130320-130000.gz',
        'pagecounts-20130320-140000.gz',
        'pagecounts-20130320-150000.gz',
        'pagecounts-20130320-160000.gz',
        'pagecounts-20130320-170000.gz',
        'pagecounts-20130320-180000.gz',
        'pagecounts-20130320-190000.gz',
        'pagecounts-20130320-200001.gz',
        'pagecounts-20130320-210000.gz',
        'pagecounts-20130320-220000.gz',
        'pagecounts-20130320-230000.gz',
        'pagecounts-20130321-000000.gz',
        'pagecounts-20130321-010000.gz',
        'pagecounts-20130321-020000.gz',
        'pagecounts-20130321-030000.gz',
        'pagecounts-20130321-040000.gz',
        'pagecounts-20130321-050000.gz',
        'pagecounts-20130321-060000.gz',
        'pagecounts-20130321-070000.gz',
        'pagecounts-20130321-080000.gz',
        'pagecounts-20130321-090001.gz',
        'pagecounts-20130321-100000.gz',
        'pagecounts-20130321-110000.gz',
        'pagecounts-20130321-120000.gz',
        'pagecounts-20130321-130000.gz',
        'pagecounts-20130321-140000.gz',
        'pagecounts-20130321-150000.gz',
        'pagecounts-20130321-160000.gz',
        'pagecounts-20130321-170000.gz',
        'pagecounts-20130321-180000.gz',
        'pagecounts-20130321-190000.gz',
        'pagecounts-20130321-200000.gz',
        'pagecounts-20130321-210001.gz',
        'pagecounts-20130321-220000.gz',
        'pagecounts-20130321-230000.gz',
        'pagecounts-20130322-000000.gz',
        'pagecounts-20130322-010000.gz',
        'pagecounts-20130322-020000.gz',
        'pagecounts-20130322-030000.gz',
        'pagecounts-20130322-040000.gz',
        'pagecounts-20130322-050000.gz',
        'pagecounts-20130322-060000.gz',
        'pagecounts-20130322-070000.gz',
        'pagecounts-20130322-080000.gz',
        'pagecounts-20130322-090001.gz',
        'pagecounts-20130322-100000.gz',
        'pagecounts-20130322-110000.gz',
        'pagecounts-20130322-120000.gz',
        'pagecounts-20130322-130000.gz',
        'pagecounts-20130322-140000.gz',
        'pagecounts-20130322-150000.gz',
        'pagecounts-20130322-160000.gz',
        'pagecounts-20130322-170000.gz',
        'pagecounts-20130322-180000.gz',
        'pagecounts-20130322-190000.gz',
        'pagecounts-20130322-200000.gz',
        'pagecounts-20130322-210000.gz',
        'pagecounts-20130322-220001.gz',
        'pagecounts-20130322-230000.gz',
        'pagecounts-20130323-000000.gz',
        'pagecounts-20130323-010000.gz',
        'pagecounts-20130323-020000.gz',
        'pagecounts-20130323-030000.gz',
        'pagecounts-20130323-040000.gz',
        'pagecounts-20130323-050000.gz',
        'pagecounts-20130323-060000.gz',
        'pagecounts-20130323-070000.gz',
        'pagecounts-20130323-080000.gz',
        'pagecounts-20130323-090000.gz',
        'pagecounts-20130323-100001.gz',
        'pagecounts-20130323-110000.gz',
        'pagecounts-20130323-120000.gz',
        'pagecounts-20130323-130000.gz',
        'pagecounts-20130323-140000.gz',
        'pagecounts-20130323-150000.gz',
        'pagecounts-20130323-160000.gz',
        'pagecounts-20130323-170000.gz',
        'pagecounts-20130323-180000.gz',
        'pagecounts-20130323-190000.gz',
        'pagecounts-20130323-200000.gz',
        'pagecounts-20130323-210000.gz',
        'pagecounts-20130323-220001.gz',
        'pagecounts-20130323-230000.gz',
        'pagecounts-20130324-000000.gz',
        'pagecounts-20130324-010000.gz',
        'pagecounts-20130324-020000.gz',
        'pagecounts-20130324-030000.gz',
        'pagecounts-20130324-040000.gz',
        'pagecounts-20130324-050000.gz',
        'pagecounts-20130324-060000.gz',
        'pagecounts-20130324-070000.gz',
        'pagecounts-20130324-080000.gz',
        'pagecounts-20130324-090001.gz',
        'pagecounts-20130324-100000.gz',
        'pagecounts-20130324-110000.gz',
        'pagecounts-20130324-120000.gz',
        'pagecounts-20130324-130000.gz',
        'pagecounts-20130324-140000.gz',
        'pagecounts-20130324-150000.gz',
        'pagecounts-20130324-160000.gz',
        'pagecounts-20130324-170000.gz',
        'pagecounts-20130324-180000.gz',
        'pagecounts-20130324-190000.gz',
        'pagecounts-20130324-200000.gz',
        'pagecounts-20130324-210001.gz',
        'pagecounts-20130324-220000.gz',
        'pagecounts-20130324-230000.gz',
        'pagecounts-20130325-000000.gz',
        'pagecounts-20130325-010000.gz',
        'pagecounts-20130325-020000.gz',
        'pagecounts-20130325-030000.gz',
        'pagecounts-20130325-040000.gz',
        'pagecounts-20130325-050000.gz',
        'pagecounts-20130325-060000.gz',
        'pagecounts-20130325-070000.gz',
        'pagecounts-20130325-080000.gz',
        'pagecounts-20130325-090001.gz',
        'pagecounts-20130325-100000.gz',
        'pagecounts-20130325-110000.gz',
        'pagecounts-20130325-120000.gz',
        'pagecounts-20130325-130000.gz',
        'pagecounts-20130325-140000.gz',
        'pagecounts-20130325-150000.gz',
        'pagecounts-20130325-160000.gz',
        'pagecounts-20130325-170000.gz',
        'pagecounts-20130325-180000.gz',
        'pagecounts-20130325-190000.gz',
        'pagecounts-20130325-200000.gz',
        'pagecounts-20130325-210001.gz',
        'pagecounts-20130325-220000.gz',
        'pagecounts-20130325-230000.gz',
        'pagecounts-20130326-000000.gz',
        'pagecounts-20130326-010000.gz',
        'pagecounts-20130326-020000.gz',
        'pagecounts-20130326-030000.gz',
        'pagecounts-20130326-040000.gz',
        'pagecounts-20130326-050000.gz',
        'pagecounts-20130326-060000.gz',
        'pagecounts-20130326-070000.gz',
        'pagecounts-20130326-080000.gz',
        'pagecounts-20130326-090001.gz',
        'pagecounts-20130326-100000.gz',
        'pagecounts-20130326-110000.gz',
        'pagecounts-20130326-120000.gz',
        'pagecounts-20130326-130000.gz',
        'pagecounts-20130326-140000.gz',
        'pagecounts-20130326-150000.gz',
        'pagecounts-20130326-160000.gz',
        'pagecounts-20130326-170000.gz',
        'pagecounts-20130326-180000.gz',
        'pagecounts-20130326-190000.gz',
        'pagecounts-20130326-200000.gz',
        'pagecounts-20130326-210001.gz',
        'pagecounts-20130326-220000.gz',
        'pagecounts-20130326-230000.gz',
        'pagecounts-20130327-000000.gz',
        'pagecounts-20130327-010000.gz',
        'pagecounts-20130327-020000.gz',
        'pagecounts-20130327-030000.gz',
        'pagecounts-20130327-040000.gz',
        'pagecounts-20130327-050000.gz',
        'pagecounts-20130327-060000.gz',
        'pagecounts-20130327-070000.gz',
        'pagecounts-20130327-080000.gz',
        'pagecounts-20130327-090001.gz',
        'pagecounts-20130327-100000.gz',
        'pagecounts-20130327-110000.gz',
        'pagecounts-20130327-120000.gz',
        'pagecounts-20130327-130000.gz',
        'pagecounts-20130327-140000.gz',
        'pagecounts-20130327-150000.gz',
        'pagecounts-20130327-160000.gz',
        'pagecounts-20130327-170000.gz',
        'pagecounts-20130327-180000.gz',
        'pagecounts-20130327-190000.gz',
        'pagecounts-20130327-200001.gz',
        'pagecounts-20130327-210000.gz',
        'pagecounts-20130327-220000.gz',
        'pagecounts-20130327-230000.gz',
        'pagecounts-20130328-000000.gz',
        'pagecounts-20130328-010000.gz',
        'pagecounts-20130328-020000.gz',
        'pagecounts-20130328-030000.gz',
        'pagecounts-20130328-040000.gz',
        'pagecounts-20130328-050000.gz',
        'pagecounts-20130328-060000.gz',
        'pagecounts-20130328-070000.gz',
        'pagecounts-20130328-080001.gz',
        'pagecounts-20130328-090000.gz',
        'pagecounts-20130328-100000.gz',
        'pagecounts-20130328-110000.gz',
        'pagecounts-20130328-120000.gz',
        'pagecounts-20130328-130000.gz',
        'pagecounts-20130328-140000.gz',
        'pagecounts-20130328-150000.gz',
        'pagecounts-20130328-160000.gz',
        'pagecounts-20130328-170000.gz',
        'pagecounts-20130328-180000.gz',
        'pagecounts-20130328-190000.gz',
        'pagecounts-20130328-200001.gz',
        'pagecounts-20130328-210000.gz',
        'pagecounts-20130328-220000.gz',
        'pagecounts-20130328-230000.gz',
        'pagecounts-20130329-000000.gz',
        'pagecounts-20130329-010000.gz',
        'pagecounts-20130329-020000.gz',
        'pagecounts-20130329-030000.gz',
        'pagecounts-20130329-040000.gz',
        'pagecounts-20130329-050000.gz',
        'pagecounts-20130329-060000.gz',
        'pagecounts-20130329-070000.gz',
        'pagecounts-20130329-080001.gz',
        'pagecounts-20130329-090000.gz',
        'pagecounts-20130329-100000.gz',
        'pagecounts-20130329-110000.gz',
        'pagecounts-20130329-120000.gz',
        'pagecounts-20130329-130000.gz',
        'pagecounts-20130329-140000.gz',
        'pagecounts-20130329-150000.gz',
        'pagecounts-20130329-160000.gz',
        'pagecounts-20130329-170000.gz',
        'pagecounts-20130329-180000.gz',
        'pagecounts-20130329-190000.gz',
        'pagecounts-20130329-200001.gz',
        'pagecounts-20130329-210000.gz',
        'pagecounts-20130329-220000.gz',
        'pagecounts-20130329-230000.gz',
        'pagecounts-20130330-000000.gz',
        'pagecounts-20130330-010000.gz',
        'pagecounts-20130330-020000.gz',
        'pagecounts-20130330-030000.gz',
        'pagecounts-20130330-040000.gz',
        'pagecounts-20130330-050000.gz',
        'pagecounts-20130330-060000.gz',
        'pagecounts-20130330-070000.gz',
        'pagecounts-20130330-080001.gz',
        'pagecounts-20130330-090000.gz',
        'pagecounts-20130330-100000.gz',
        'pagecounts-20130330-110000.gz',
        'pagecounts-20130330-120000.gz',
        'pagecounts-20130330-130000.gz',
        'pagecounts-20130330-140000.gz',
        'pagecounts-20130330-150000.gz',
        'pagecounts-20130330-160000.gz',
        'pagecounts-20130330-170000.gz',
        'pagecounts-20130330-180000.gz',
        'pagecounts-20130330-190000.gz',
        'pagecounts-20130330-200001.gz',
        'pagecounts-20130330-210000.gz',
        'pagecounts-20130330-220000.gz',
        'pagecounts-20130330-230000.gz',
        'pagecounts-20130331-000000.gz',
        'pagecounts-20130331-010000.gz',
        'pagecounts-20130331-020000.gz',
        'pagecounts-20130331-030000.gz',
        'pagecounts-20130331-040000.gz',
        'pagecounts-20130331-050000.gz',
        'pagecounts-20130331-060000.gz',
        'pagecounts-20130331-070000.gz',
        'pagecounts-20130331-080000.gz',
        'pagecounts-20130331-090001.gz',
        'pagecounts-20130331-100000.gz',
        'pagecounts-20130331-110000.gz',
        'pagecounts-20130331-120000.gz',
        'pagecounts-20130331-130000.gz',
        'pagecounts-20130331-140000.gz',
        'pagecounts-20130331-150000.gz',
        'pagecounts-20130331-160000.gz',
        'pagecounts-20130331-170000.gz',
        'pagecounts-20130331-180000.gz',
        'pagecounts-20130331-190000.gz',
        'pagecounts-20130331-200001.gz',
        'pagecounts-20130331-210000.gz',
        'pagecounts-20130331-220000.gz',
        'pagecounts-20130331-230000.gz'
    ]

    # md5 checksum hashes to python
    dt_md5 = 'md5sums.txt'
    dt_pd_md5 = pd.read_table(os.path.dirname(os.path.realpath(__file__)) + sl + dt_md5, delim_whitespace=True,
                              header=None, names=['md5', 'fname'], index_col=1, dtype={'md5': str, 'fname': str})

    dt_pd_wiki_legacy = pd.DataFrame(columns=['project', 'page_title', 'counter', 'rsize', 'tstamp'])
    # dt_pd_wiki_legacy['tstamp'] = pd.to_datetime(dt_pd_wiki_legacy['tstamp'])
    dt_pd_wiki_legacy.set_index('page_title', inplace=True, drop=True, append=False, verify_integrity=True)

    t = 0
    for x in files:
        if hashlib.md5(open(x, 'rb').read()).hexdigest() == dt_pd_md5.loc[x]['md5']:
            print('md5 match', x)
            try:
                f = gzip.open(x, 'rb')
                file_content = f.read()
                f.close()
                winp = io.StringIO(file_content.decode('utf-8', errors='replace'), newline='\n')
                wframe = pd.read_table(winp, sep=' ', usecols=[0, 1, 2, 3],
                                       names=['project', 'page_title', 'counter', 'rsize'], index_col=['page_title'],
                                       # warn_bad_lines=True,
                                       skiprows=range(0, 1),
                                       # dtype={'project': str, 'page_title': str, 'counter': int, 'rsize': float},
                                       error_bad_lines=False,
                                       # converters={'project': str, 'page_title': str, 'counter': int, 'rsize': float},
                                       # low_memory=False,
                                       )
                try:
                    wframe = wframe.loc['Bitcoin']
                    # wframe['tstamp'] = pd.to_datetime(dt.datetime.strptime(x[11:-3], "%Y%m%d-%H%M%S"))
                    wframe['tstamp'] = x[11:-3]
                    dt_pd_wiki_legacy = dt_pd_wiki_legacy.append(wframe)
                    dt_pd_wiki_legacy['tstamp'] = pd.to_datetime(dt_pd_wiki_legacy['tstamp'])
                    print('----------------------------')
                    print(t)
                    print('progres: ', round((t / len(files))*100, 1), "%")
                    dt_pd_wiki_legacy.to_pickle('dt_pd_wiki_legacy.pickle')
                    t = t + 1
                except Exception:
                    print('error in (no bitcoin article retrives): ',x)
            except Exception:
                # raise
                print('gzip open error in ', x)
        else:
            print('------------------------------------------------------')
            print('MD5 error in file', x)
            print('------------------------------------------------------')

    # dt_pd_wiki_legacy['tstamp'] = pd.to_datetime(dt_pd_wiki_legacy['tstamp'])
    print(time.strftime("%H:%M:%S"))
    print('current cycle of scraping done')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")