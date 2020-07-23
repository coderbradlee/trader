# coding: utf-8
import ths
import time

if __name__ == "__main__":
    x = ths.Ths()
    print("余额", x.balance())
    x.buy("510050", 3.36, 100)
    time.sleep(5)
    x.sell("510050", 3.36, 100)
    time.sleep(3)
    # print("今日委托，包含已撤单", x.today_entrusts())
    canCancel = x.cancel_entrusts()
    print("可撤单", canCancel)
    for c in canCancel:
        print("撤单", c.get("合同编号"))
        x.cancel_entrust(c.get("合同编号"))
    # time.sleep(3)
    # print("今日成交", x.today_trades())
