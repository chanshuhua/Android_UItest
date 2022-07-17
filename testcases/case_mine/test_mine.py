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
@allure.feature("test_mine")
@pytest.mark.usefixtures("allure_getreport")
class Test_Mine:

    def test_login(self):
        print("1")
        assert 1 == 1



# if __name__ == '__main__':
    # pytest.main(['-sv','test_mine.py','--alluredir','./report'])
    # sleep(1)
    # os.system("allure serve allure ")
