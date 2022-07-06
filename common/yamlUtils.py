#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/6 19:30
# @Author  : chenshuhua
# @File    : yamlUtils.py

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
            data = yaml.load(stream=file, Loader=yaml.FullLoader)
            tests = data['tests']
            print(tests)
            for its in tests:
                print(its)
                case.append(its.get('case'))
                param.append(its.get('param'))
                expected.append(its.get('expected'))
            # print(case,param,expected)
            # parameters = zip(case, param, expected)
            # print(list(parameters))
            #     description.append.get('description'))
                print((its['case']['description']))


if __name__ == '__main__':
    YamlUtils().get_yaml_data(path=path.FilePath().find_by_filename(filname='test.yaml'))




