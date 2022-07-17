import logging
import os
import time
import allure
import pytest
from appium import webdriver
from common.branchCheck import branchCheck
from common.log import Logger

global driver
global desired_caps
desired_caps = dict(branchCheck().confdata)

@pytest.fixture(scope="session")
def driver_operation():
    try:
        # desired_caps = dict(branchCheck().confdata)
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # 后置关闭
        # yield driver
        # time.sleep(1)
        # driver.close_app()
        # print("\n关闭driver")

    except IOError:
        Logger.logger()


@pytest.fixture(scope="session")
def env():
    allure.description(desired_caps)
    return


@pytest.fixture(scope="session")
def allure_getreport():
    yield
    # os.system()
    os.system("allure generate ./reports/allure-temp -o ./reports/allure-html --clean")
    time.sleep(2)
    os.system("allure open ./reports/allure-html")
    print("allure-report is opened...")



# if __name__ == '__main__':
    # driver_operation()