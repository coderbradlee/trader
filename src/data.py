# coding: utf-8
from __future__ import print_function
from __future__ import division

import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

import os
import sys
import abupy
from abupy import abu, EMarketTargetType, AbuMetricsBase, ABuMarketDrawing, ABuProgress, ABuSymbolPd, get_price, ABuIndustries
from abupy import EMarketDataFetchMode, EDataCacheType, EMarketSourceType, FuturesBaseMarket, TCBaseMarket, ABuDateUtil
from abupy import AbuDataParseWrap, StockBaseMarket, SupportMixin, ABuNetWork, Symbol, code_to_symbol

class data:
    def __init__(self):
        abupy.env.disable_example_env_ipython()
        abupy.env.g_data_fetch_mode = EMarketDataFetchMode.E_DATA_FETCH_NORMAL
        abupy.env.g_data_cache_type = EDataCacheType.E_DATA_CACHE_CSV
        abupy.env.g_project_data_dir="../data"

    def test(self):
        ABuSymbolPd.make_kl_df('usBIDU').tail()

    def testtx(self):
        abupy.env.g_market_source = EMarketSourceType.E_MARKET_SOURCE_tx
        abu.run_kl_update(start='2011-08-08', end='2017-08-08', market=EMarketTargetType.E_MARKET_TARGET_US, n_jobs=10)

    def testbd(self):
        abupy.env.g_market_source = EMarketSourceType.E_MARKET_SOURCE_bd
        abu.run_kl_update(start='2011-08-08', end='2017-08-08', market=EMarketTargetType.E_MARKET_TARGET_CN, n_jobs=10)
    def testnt(self):
        abupy.env.g_market_source = EMarketSourceType.E_MARKET_SOURCE_nt
        abu.run_kl_update(start='2011-08-08', end='2017-08-08', market=EMarketTargetType.E_MARKET_TARGET_HK, n_jobs=10)
    def testsn(self):
        abupy.env.g_market_source = EMarketSourceType.E_MARKET_SOURCE_sn_futures
        abu.run_kl_update(start='2011-08-08', end='2017-08-08', market=EMarketTargetType.E_MARKET_TARGET_FUTURES_CN,
                          n_jobs=4)







