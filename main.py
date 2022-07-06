# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from copy import copy, deepcopy
import datetime

from appium import webdriver
# 初始化参数
desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '11',  # 手机安卓版本
    'deviceName': 'xxx',  # 设备名，安卓手机可以随意填写
    'appPackage': 'com.theswitchbot.switchbot',  # 启动APP Package名称
    'appActivity': '.index.ui.SplashActivity',  # 启动Activity名称
    'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
    'resetKeyboard': True,  # 执行完程序恢复原来输入法
    'noReset': True,  # 不要重置App，如果为False的话，执行完脚本后，app的数据会清空，比如你原本登录了，执行完脚本后就退出登录了
    'newCommandTimeout': 6000,
    # 'automationName': 'UiAutomator2'
}
# 连接Appium Server，初始化自动化环境
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 日出前5
    n0 = 25920 -32.4295165;-3.8566736
    print(convert(n0))
    # 日出时
    n1 = 26220
    print(convert(n1))
    # 日出后5min
    n2 = 30060
    print(convert(n2))

    s0 = 41160
    s1 = 38160
    print(convert(s0))
    print(convert(s1))
