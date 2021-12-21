# -*- coding: utf-8 -*-

import ccxt

# 交易所API账户配置
accountConfig = {
    'apiKey': '029a61a7-34dc-42fd-a9d0-cd06302a452a',
    'secret': '1055D7529E08D0F4D942164D1E8A49A3',
    'password': '123456789a',
    'enable_proxies': True,
    'proxies': {
        'http': "http://127.0.0.1:10800",  # these proxies won't work for you, they are here for example
        'https': "http://127.0.0.1:10800",
    }
}


# CCXT初始化
exchange = ccxt.okex5(config={
    'enableRateLimit': True,
    'apiKey': accountConfig['apiKey'],
    'secret': accountConfig['secret'],
    # okex requires this: https://github.com/ccxt/ccxt/wiki/Manual#authentication
    'password': accountConfig['password'],
    'verbose': False,  # for debug output
})
if accountConfig['enable_proxies'] is True:
    exchange.proxies = accountConfig['proxies']

paramss = {
    "instId":"SHIB-USDT-SWAP",
    "tdMode":"isolated",
    "side":"buy",
    "ordType":"conditional",
    "sz":"1",
    "tpTriggerPx":"0.00002800",
    "tpOrdPx":"0.00002800"
}

privatePostAccountSetLeverageRes = exchange.privatePostTradeOrderAlgo(params=paramss)

print(privatePostAccountSetLeverageRes)