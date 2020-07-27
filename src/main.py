# coding: utf-8
import easyquant
from easyquant import DefaultQuotationEngine, DefaultLogHandler, PushBaseEngine
def startTHS():
    broker = 'ths'
    need_data = "ht.json"
    quotation_engine = DefaultQuotationEngine
    quotation_engine.PushInterval = 10
    log_handler = DefaultLogHandler(name='macd', log_type="file", filepath="engine.log")

    m = easyquant.MainEngine(broker, need_data, quotation_engines=[quotation_engine], log_handler=log_handler)
    # m.is_watch_strategy = True  # 策略文件出现改动时,自动重载,不建议在生产环境下使用
    m.load_strategy()
    m.start()


if __name__ == "__main__":
    startTHS()
