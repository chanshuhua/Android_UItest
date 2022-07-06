#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/6 19:30
# @Author  : chenshuhua
# @File    : yamlUtils.py

import yaml


class YamlUtils:
    '''
    获取yaml文件内容
    '''

    def get_yaml_data(self, path):
        '''
        获取yaml文件内容
        :param path: 文件路径
        :return: 返回内容
        '''
        # 约定yaml文件格式
        case = []
        param = []
        expected = []




        with open(path, "r+", encoding="utf-8") as file:
            data = yaml.load(stream=file, Loader=yaml.FullLoader)
            return data

