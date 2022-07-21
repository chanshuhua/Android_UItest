#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/28 10:23
# @Author  : chenshuhua
# @File    : log.py
'''日志相关'''
import logging
import os
from datetime import datetime

from common.path import FilePath


timenow = str(datetime.today().strftime('%Y-%m-%d'))
print(timenow)

class Logger:
    '''未完善 用pytest本身的logcli'''
    # TODO

    global timenow

    @classmethod
    def logdir(cls):

        cls.LOGS_DIR = FilePath().find_by_dirname('testlog')
        print(cls.LOGS_DIR)
        return cls.LOGS_DIR

    @classmethod
    def logger(cls):
        # log_cli = 1  # 代表ture 1代表执行日志显示更详细
        # log_cli_level = DEBUG  # 代表日志级别
        # log_cli_date_format = % Y: % m: % d % H: % M: % S  # 代表日志时间
        # log_cli_format = % (asctime)s - % (filename)s - % (module)s - % (funcName)s - % (lineno)d - % (levelname)s - % (message)s  # 代表日志格式
        # log_file =./ logs / test.log  # 代表日志输入文件路径 项目根目录下的logs文件中
        # log_file_level = DEBUG
        # log_file_date_format = % Y: % m: % d % H: % M: % S
        # log_file_format = % (asctime)s - % (filename)s - % (module)s - % (funcName)s - % (lineno)d - % (levelname)s - % (message)s


        # 日志配置项
        log_name = "log"
        log_level_input = "DEBUG"
        log_level_console_output = "INFO"
        log_level_file_output = "INFO"
        log_file_name = "{}.log".format(timenow)
        log_formatter = "%(asctime)s - [%(levelname)s] - [%(filename)s - %(funcName)s]: %(message)s"

        # # （每创建一个对象，日志收集器的名字如果不一致，创建两个或者以上的对象，使用一个对象来打印日志，打印日志的次数只有一次）
        # my_log = logging.getLogger(log_name)
        # 设置日志收集器，设置日志收集器等级（日志收集器的名字如果一致，创建两个或者以上的对象，使用一个对象来打印日志，打印日志的次数和创建对象的数量一致）
        my_log = logging.getLogger(log_name)
        my_log.setLevel(log_level_input)
        # 设置日志输出格式
        str_form = log_formatter
        formater = logging.Formatter(str_form)
        # 设置日志输出渠道，设置日志输出渠道等级
        sh = logging.StreamHandler()
        sh.setLevel(log_level_console_output)
        sh.setFormatter(formater)
        # 将输出渠道添加到日志收集器中
        my_log.addHandler(sh)
        # 设置日志输出到文件的渠道,设置日志输出渠道等级
        fh = logging.FileHandler(filename=os.path.join(cls.logdir(), log_file_name),
                                 encoding="utf-8")
        fh.setLevel(log_level_file_output)
        fh.setFormatter(formater)
        # 将输出到文件渠道添加到日志收集器中
        my_log.addHandler(fh)

        return my_log


# log = Logger.create_logger()


if __name__ == '__main__':
    log = Logger.logger()