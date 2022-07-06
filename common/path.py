#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/28 13:11
# @Author  : chenshuhua
# @File    : path.py
import os


class FilePath:
    '''
    找到文件路径并访问
    '''
    def __init__(self):
        '''
        字典对象维护目录结构
        '''
        self.dir={
            'testlog':'testlog',
            'testdata':'testdata',
            'testcases':'testcases',
            'yamldata':'testdata/yamldata'
        }
        self.file = {
            'test.txt':'*.text'
        }

    def find_absopath(self):
        # 找到根目录
        PROJECT_ABSOLUTE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.project_absolute_path = PROJECT_ABSOLUTE_PATH   # 反斜杠
        return self.project_absolute_path

    def find_by_dirname(self,dirname):
        '''
        拼接目录
        :return:
        '''
        try:
            if not self.dir.get(dirname):
                os.chdir(self.find_absopath())
                os.makedirs(dirname)
                self.dir[dirname] = 'newadd_dir_%s' %(dirname)
            self.dirname = self.dir[dirname]
            destin_path = os.path.join(self.find_absopath(),self.dirname).replace('\\','/')
            return destin_path
        except Exception as e:
            return False,"cannot find the dirname {} ,maybe its a filename.".format(dirname)

    def find_by_filename(self,filname):
        '''
        拼接文件
        :return:
        '''
        try:
            if filname.endswith(".log"):
                return os.path.join(self.find_absopath(),self.dir['testlog'],filname).replace('\\','/')
            if filname.endswith(".yaml"):
                return os.path.join(self.find_absopath(), self.dir['yamldata'],filname).replace('\\', '/')
            self.filename = self.file[filname]
            destin_path = os.path.join(self.find_absopath(),self.filename).replace('\\','/')
            return destin_path
        except Exception as e:
            return False,"cannot find the filename {} ,maybe its a dirname.".format(filname)



if __name__ == '__main__':
    # print(os.path.dirname('tesss'))
    # print(FilePath().find_by_dirname('testss'))
    # print(FilePath().find_by_filename('test.yaml'))
    # print(FilePath().find_by_filename('test.txt'))

    pass