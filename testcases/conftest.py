import logging

import pytest
from appium import webdriver
from common.branchCheck import branchCheck
from common.log import Logger


@pytest.fixture(scope="function",name="case_init")
def case_init():
    desired_caps = dict(branchCheck().confdata)
    print(desired_caps)
    Logger().info(desired_caps)
    webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


