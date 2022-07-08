#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/8 10:49
# @Author  : chenshuhua
# @File    : branchCheck.py
import configparser

from appium import webdriver
from common.path import FilePath


class branchCheck:
    '''
    获取设备信息
    '''
    def __init__(self):

        self.conf_name = []
        self.conf_value = []
        # 连接Appium Server，初始化自动化环境
        self.driver = object
        self.confdata = self.get_config()

    def get_config(self):
        '''
        获取conf.ini文件内容
        :return:
        '''
        conf_path = FilePath().find_by_filename('conf.ini')
        self.conf = configparser.ConfigParser()
        self.conf.read(conf_path, encoding='utf-8')
        self.conf_name = self.conf.options('config')
        for name in self.conf_name:
            self.conf_value.append(self.conf.get('config',name))
        conf_data = zip(self.conf_name,self.conf_value)
        return conf_data



if __name__ == '__main__':
    print(list(branchCheck().confdata))