#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Android_UItest 
@File    ：test_login.py.py
@IDE     ：PyCharm 
@Author  ：chenshuhua
@Date    ：2022/7/10 14:07 
'''
import os
from time import sleep

import allure
import pytest


@pytest.mark.usefixtures("driver_operation")
@allure.feature("我的页面")
class Test_Mine:

    def test_login(self):
        assert 1 == 1



if __name__ == '__main__':
    pytest.main(['-sv','test_mine.py'])
    sleep(1)
    os.system("allure generate ./././report/temp -o ./report/allure_reports --clean ")