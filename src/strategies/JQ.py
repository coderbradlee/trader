# coding:utf8

import jqdatasdk


class JQ():
    def __init__(self, user, password):
        jqdatasdk.auth(user, password)

    def get_price(self, stockcode):
        return jqdatasdk.get_price(stockcode)
