#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/28 10:23
# @Author  : chenshuhua
# @File    : log.py
'''日志相关'''
import logging
import os
from config_utils import filepath


class Logger(object):


    def logdir(cls):

        cls.LOGS_DIR = filepath.FilePath().find_by_dirname('testlog')
        print(cls.LOGS_DIR)
        return cls.LOGS_DIR

    @classmethod
    def create_logger(cls):
        # 日志配置项
        log_name = "log"
        log_level_input = "DEBUG"
        log_level_console_output = "INFO"
        log_level_file_output = "INFO"
        log_file_name = "test.log"
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
                                 encoding="utf8")
        fh.setLevel(log_level_file_output)
        fh.setFormatter(formater)
        # 将输出到文件渠道添加到日志收集器中
        my_log.addHandler(fh)

        return my_log


# log = Logger.create_logger()


if __name__ == '__main__':
    log = Logger.create_logger()