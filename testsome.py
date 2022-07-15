#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/7 11:08
# @Author  : chenshuhua
# @File    : testsome.py
import datetime

# import TimezoneFinder as TimezoneFinder
import pytz
from tzwhere import tzwhere


def convert(seconds):

    # seconds = seconds % (24 * 3600)
    #
    # hour = seconds // 3600
    #
    # seconds %= 3600
    #
    # minutes = seconds // 60
    #
    # seconds %= 60
    #
    # return "%02d:%02d:%02d" % (hour, minutes, seconds) #formatting

    return str(datetime.timedelta(seconds=seconds))




def timez(longitude,latitude):
    tz = tzwhere.tzwhere()
    time_zone = tz.tzNameAt(longitude,latitude)
    # tf = TimezoneFinder()
    print("地区:{}".format(time_zone))
    # time = pytz.timezone(tf.timezone_at(lng=longitude, lat=latitude)).localize(
    #     datetime.datetime(2022, 7, 8)).strftime('%z')

    # # invert sign and return in 'Etc/GMT' format
    # if time[0] == '-':
    #     time_zone = 'Etc/GMT+' + time[2]
    # else:
    #     time_zone = 'Etc/GMT-' + time[2]

if __name__ == '__main__':
    timez(31.230416,121.473701)
    print(convert(75780))
    print(convert(39540))
    print(convert(56760))