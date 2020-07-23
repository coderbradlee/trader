# coding: utf-8
import sys
import easytrader
import time

IS_WIN_PLATFORM = sys.platform != "darwin"

def robust(actual_do):
    def add_robust(*args, **keyargs):
        try:
            return actual_do(*args, **keyargs)
        except Exception as e:
            print(actual_do.__name__, repr(e))
            # print(traceback.format_exc())
    return add_robust


class Ths:
    def __init__(self):
        self._user = easytrader.use('ths')
        self._user.connect(r'C:\同花顺软件\同花顺\xiadan.exe')  # 类似 r'C:\htzqzyb2\xiadan.exe'
        self._user.enable_type_keys_for_editor()

    # {'资金余额': 198552.17, '可用金额': 198552.17, '可取金额': 0.0, '股票市值': 333.1, '总资产': 198885.27}
    @robust
    def balance(self):
        time.sleep(3)
        return self._user.balance

    # [{'委托时间': '17:36:16', '证券代码': '510050', '证券名称': '上证50ETF', '操作': '卖出', '备注': '未成交', '委托数量': 1, '成交数量': 0,
    #   '委托价格': 6.66, '成交均价': 0.0, '撤消数量': 0, '合同编号': '1647464645', '交易市场': '上海Ａ股', '股东帐户': 'A444334465',
      # 'Unnamed: 13': ''}]
    @robust
    def today_entrusts(self):
        return self._user.today_entrusts

    # 当日成交
    @robust
    def today_trades(self):
        return self._user.today_trades

    @robust
    def cancel_entrusts(self):
        return self._user.cancel_entrusts

    @robust
    def cancel_entrust(self, id):
        return self._user.cancel_entrust(id)

    @robust
    def sell(self, security, price=0, amount=0):
        return self._user.sell(security, price, amount)

    @robust
    def buy(self, security, price=0, amount=0):
        return self._user.buy(security, price, amount)

    @robust
    def auto_ipo(self):
        self._user.auto_ipo()