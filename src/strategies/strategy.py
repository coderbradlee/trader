import time
import datetime as dt
from dateutil import tz
from easyquant import DefaultLogHandler
from easyquant import StrategyTemplate
import jqdatasdk


# class JQ():
#     def __init__(self, user, password):
#         # https: // www.joinquant.com / help / api / help?name = JQData
#         jqdatasdk.auth(user, password)
#
#     def get_price(self, security, start_date=None, end_date=None, frequency='daily',
#               fields=None, skip_paused=False, fq='pre', count=None, panel=True, fill_paused=True):
#         return jqdatasdk.get_price(security, start_date=None, end_date=None, frequency='daily',
#               fields, skip_paused=False, fq='pre', count=None, panel=True, fill_paused=True)





class Strategy(StrategyTemplate):
    name = 'jq'

    # def init(self):
    #     # 通过下面的方式来获取时间戳
    #     now_dt = self.clock_engine.now_dt
    #     now = self.clock_engine.now
    #     now = time.time()
    #
    #     # 注册时钟事件
    #     clock_type = "盘尾"
    #     moment = dt.time(14, 56, 30, tzinfo=tz.tzlocal())
    #     self.clock_engine.register_moment(clock_type, moment)
    #
    #     # 注册时钟间隔事件, 不在交易阶段也会触发, clock_type == minute_interval
    #     minute_interval = 1.5
    #     self.clock_engine.register_interval(minute_interval, trading=False)

    def strategy(self, event):
        # balances = self.user.balance.copy()
        # print(balances)
        # self.log.info('行情数据: 万科价格: %s' % event.data['000002'])
        # self.log.info("balance: %s" % balances)
        # self.log.info('行情数据: 万科价格: %s' % self.jq.get_price('000002.XSHE'))
        print("what")
        # df = self.jq.get_price('000002.XSHE', start_date='2015-01-01', end_date='2015-01-02 23:00:00', frequency='minute')
        df = jqdatasdk.get_price('000002.XSHE', start_date='2020-07-27', end_date='2020-07-27 23:00:00', frequency='minute')
        print("df", df.head())

        # self.log.info('\n')

    def clock(self, event):
        """在交易时间会定时推送 clock 事件
        :param event: event.data.clock_event 为 [0.5, 1, 3, 5, 15, 30, 60] 单位为分钟,  ['open', 'close'] 为开市、收市
            event.data.trading_state  bool 是否处于交易时间
        """
        if event.data.clock_event == 'open':
            # 开市了
            self.log.info('open')
        elif event.data.clock_event == 'close':
            # 收市了
            self.log.info('close')
        # elif event.data.clock_event == 0.5:
        #     # 5 分钟的 clock
        #     self.log.info("0.5分钟")
        #     self.log.info('行情数据: 万科价格: %s' % self.jq.get_price('000002.XSHE'))

    def log_handler(self):
        """自定义 log 记录方式"""
        return DefaultLogHandler(self.name, log_type='file', filepath='strategy.log')

    def shutdown(self):
        """
        关闭进程前的调用
        :return:
        """
        self.log.info("假装在关闭前保存了策略数据")
