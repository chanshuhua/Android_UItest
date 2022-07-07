#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/6 19:30
# @Author  : chenshuhua
# @File    : yamlUtils.py
import json

import yaml

from common import path


class YamlUtils:
    '''
    获取yaml文件内容
    '''

    def get_yaml_data(self,path):
        '''
        获取yaml文件内容
        :param path: 文件路径
        :return: 返回内容
        '''
        # 约定yaml文件格式
        case = []
        param = []
        expected = []

        description = []
        level = []
        author = []
        update = []

        with open(path, "r+", encoding="utf-8") as file:
            # dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
            data = yaml.load(file.read(), Loader=yaml.FullLoader)
            tests = data['tests']
            print(tests)
            for its in tests:
                case.append(its.get('case'))
                param.append(its.get('param'))
                expected.append(its.get('expected'))
            for ca in case:
                description.append(ca.get('description'))
                level.append(ca.get('level'))
                author.append(ca.get('author'))
                update.append(ca.get('update'))

            parameters = zip(description,level,author,update, param, expected)
            print(list(parameters))



if __name__ == '__main__':
    YamlUtils().get_yaml_data(path=path.FilePath().find_by_filename(filname='test.yaml'))




