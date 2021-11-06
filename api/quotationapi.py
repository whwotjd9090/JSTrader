# -*- coding:utf-8 -*-


import datetime
import pytz
import requests
import json
from typing import Dict, List, Optional
from .config import upbitconf


def get_header() -> Dict[str, str]:
    """Get Upbit Quotation API Header

    Get dict {'Accept': 'application/json'}

    Returns:
        Upbit Quotation API Header
    """
    return {'Accept': 'application/json'}


def get_markets(market_type: str = 'ALL') -> List[str]:
    """Get market list

    Get list of markets that can be traded within the 'market_type'

    Args:
        market_type: ALL | KRW | BTC | USDT

    Returns:
        List of markets
    """
    if market_type not in ['ALL', 'KRW', 'BTC', 'USDT']:
        raise ValueError("'market_type' must be one of ['ALL', 'KRW', 'BTC', 'USDT']")

    response = requests.get(url=upbitconf.URL.MARKET_ALL, headers=get_header())

    markets = [market['market'] for market in json.loads(response.text)]

    if market_type == 'ALL':
        return markets
    else:
        return [market for market in markets if market.startswith(market)]


def get_krw_markets() -> List[str]:
    return get_markets('KRW')


def get_btc_markets() -> List[str]:
    return get_markets('BTC')


def get_usdt_markets() -> List[str]:
    return get_markets('USDT')


def get_minute_candle(market: str,
                      unit: int,
                      to: Optional[datetime.datetime] = None,
                      count: int = 1) -> List[Dict[str, str]]:
    if unit not in [1, 3, 5, 10, 15, 30, 60, 240]:
        raise ValueError("'unit' must be one of [1, 3, 5, 10, 15, 30, 60, 240]")

    param: Dict[str, str] = {
        'market': market,
        'count': str(count)
    }

    if to and to.tzinfo:
        param['to'] = to.astimezone(pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')
        print('param_to : ', param['to'])

    response = requests.get(url=f'{upbitconf.URL.CANDLE_MINUTE}/{unit}', headers=get_header(), params=param)

    return json.loads(response.text)


# def get_day_candle(market: str, to: str = None, count: int = 1, convert) -> List[Dict[str, str]]:
#     param: Dict[str, str] = {
#         'market': market,
#         'count': str(count)
#     }
#
#     if to:
#         try:
#             datetime.datetime.strptime(to, 'yyyy-MM-dd HH:mm:ss')
#             param['to'] = to
#         except ValueError:
#             pass
#
#     response = requests.get(url=upbitconf.URL.CANDLE_DAY, headers=get_header(), params=param)
#
#     return json.loads(response.text)
