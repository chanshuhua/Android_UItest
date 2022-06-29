
from appium import webdriver

class BasePage:
    '''
    页面基类
    封装driver基本方法
    '''

    def __init__(self,driver):
        '''
        构造函数
        :param driver:
        '''
        self.driver = driver

    def locator(self,*loc):
        '''
        定位元素方法
        :param loc:
        :return:
        '''
        return self.driver.find_element(*loc)

    def input(self,loc,value):
        '''
        输入元素
        :param loc:
        :param value:
        :return:
        '''
        self.locator(loc).send_keys(value)

    def click(self,loc):
        '''
        点击元素
        :param loc:
        :return:
        '''
        self.locator(loc).click()

    def clear(self,loc):
        '''
        清空文本框内容
        :param loc:
        :return:
        '''
        self.locator(loc).clear()

    def find_textBycss(self,loc):
        '''
        根据css元素筛选框获取对象文本内容
        :param loc:
        :return:
        '''
        return self.driver.find_element_by_css_selector(*loc).text

