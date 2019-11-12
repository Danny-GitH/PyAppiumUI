#!/usr/bin/env python
# coding:utf-8
__author__ = 'dingrui'
import time
import re
import sys
import unittest
reload(sys)
sys.setdefaultencoding('utf-8')
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from comm_method.Setup_app import Start_App_Para

def get_driver():
    # 获取app启动参数
    server, desired_caps = Start_App_Para()
    driver = webdriver.Remote(server, desired_caps)
    wait = WebDriverWait(driver, 20)
    return driver, wait
