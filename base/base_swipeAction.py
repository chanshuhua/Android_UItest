#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/27 10:40
# @Author  : chenshuhua
# @File    : base_swipeAction.py.py
class BaseSwipeAction:
    def __init__(self,driver):
        self.driver = driver

    def swipe(self,start_x_ratio,start_y_ratio,end_x_ratio,end_y_ratio,duration=0):
        '''
        横向滑动
        Usage:
            driver.swipe(100, 100, 100, 400)

        :param start_x_ratio: 横坐标百分比
        :param start_y_ratio: 纵坐标百分比
        :param end_x_ratio:  横坐标百分比
        :param end_y_ratio: 纵坐标百分比
        :param duration:
        :return:
        '''
        # 获取屏幕尺寸
        window_size = self.driver.get_window_size()
        x = window_size["width"]
        y = window_size["height"]

        # 滑动百分比
        self.driver.swipe(start_x=x * start_x_ratio,
                          start_y=y * start_y_ratio,
                          end_x=x * end_x_ratio,
                          end_y=y * end_y_ratio,
                          duration=duration)

    def swipe_left(self):
        '''
        左滑
        :return:
        '''
        self.swipe(0.8, 0.8, 0.2, 0.8)

    def swipe_right(self):
        '''
        右滑
        :return:
        '''
        self.swipe(0.2, 0.8, 0.8, 0.8)

    def swipe_up(self):
        '''
        上滑，加载更多数据
        :return:
        '''
        self.swipe(0.5, 0.8, 0.5, 0.2)

    def swipe_down(self):
        '''
        下滑，刷新
        :return:
        '''
        self.swipe(0.5, 0.2, 0.5, 0.8)