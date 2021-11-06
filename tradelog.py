# -*- coding:utf-8 -*-


import os
import logging
from logging.handlers import TimedRotatingFileHandler


log_formatter = logging.Formatter('[%(asctime)s]:%(message)s')

trade_log_path = f'{os.path.dirname(os.path.abspath(__file__))}/logs/trade.log'
trade_log_handler = TimedRotatingFileHandler(filename=trade_log_path, when='D', encoding='UTF-8', utc=True)
trade_log_handler.setFormatter(log_formatter)
trade_logger = logging.getLogger('tradelog')
trade_logger.setLevel(logging.INFO)
trade_logger.addHandler(trade_log_handler)
TradeLogger = trade_logger
