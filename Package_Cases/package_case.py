#!/usr/bin/env python
# coding:utf-8
__author__ = 'dingrui'

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
# from log import Log

success = "SUCCESS   "
fail = "FAIL   "
# logger = Log()


class PackageCase(object):
    """

    """

    def __init__(self, server = None, desired_caps = None):
        if server is None or desired_caps is None:
            print "connect the telephone is fail, please reconnect!"
        else:
            self.driver = webdriver.Remote(server,desired_caps)
            driver = self.driver
            self.wait = WebDriverWait(driver, 30)
            wait = self.wait
