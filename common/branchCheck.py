#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/8 10:49
# @Author  : chenshuhua
# @File    : branchCheck.py
import configparser
from common.path import FilePath



class MyConfigParser(configparser.ConfigParser):
    def optionxform(self, optionstr):
        return optionstr


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
        self.conf = MyConfigParser()
        self.conf.read(conf_path,encoding='utf-8')
        conf_data = dict(self.conf.items(section='config'))
        for data in conf_data:
            if conf_data[data].lower() == 'true':
                conf_data[data] = True
            elif conf_data[data].lower() == 'false':
                conf_data[data] = False
        return conf_data




if __name__ == '__main__':
    print(branchCheck().confdata)