# -*- coding:utf-8 -*-


from .securityconf import UpbitSecurity


class KEY:
    ACCESS = UpbitSecurity.ACCESS_KEY
    SECURITY = UpbitSecurity.SECRET_KEY


class URL:
    BASE = 'https://api.upbit.com/v1'
    MARKET_ALL = f'{BASE}/market/all'
    CANDLE = f'{BASE}/candles'
    CANDLE_MINUTE = f'{CANDLE}/minutes'
    CANDLE_DAY = f'{CANDLE}/days'
    CANDLE_WEEK = f'{CANDLE}/weeks'
    CANDLE_MONTH = f'{CANDLE}/months'
