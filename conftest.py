import logging
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
        yield driver
        time.sleep(10)
        driver.close_app()
        print("\n关闭driver")

    except IOError:
        Logger.logger()


@pytest.fixture(scope="session")
def env():
    allure.description(desired_caps)
    return