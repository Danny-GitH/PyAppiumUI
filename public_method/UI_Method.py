#!/usr/bin/env python
# coding:utf-8
__author__ = 'dingrui'
import time
import re
import sys
import unittest
reload(sys)
#sys.setdefaultencoding('utf8')
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from comm_method.Setup_app import Start_App_Para
from Get_Device_Info.Get_Driver import *
from appium.webdriver.common.touch_action import TouchAction

success = "SUCCESS   "
fail = "FAIL   "
driver, wait = get_driver()

class PySelenuim(object):

    #presence_of_element_located((By.ID))用法
    def by_element(self, css, value):
        if css == "id":
            css_ele = wait.until(EC.presence_of_element_located((By.ID, value)))
            return css_ele
        elif  css == "name":
            css_ele = wait.until(EC.presence_of_element_located((By.NAME, value)))
            return css_ele
        elif  css == "class":
            css_ele = wait.until(EC.presence_of_element_located((By.CLASS_NAME, value)))
            return css_ele
        elif  css == "link_text":
            css_ele = wait.until(EC.presence_of_element_located((By.LINK_TEXT, value)))
            return css_ele
        elif  css == "xpath":
            css_ele = wait.until(EC.presence_of_element_located((By.XPATH, value)))
            return css_ele
        elif  css == "css":
            css_ele = wait.until(EC.presence_of_element_located((By.CLASS_NAME, value)))
            return css_ele
        else:
            return False
            #raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")

    def by_element_dr(self, css, value):
        if css == "id":
            css_ele = driver.find_element_by_id(value)
            return css_ele
        elif  css == "name":
            css_ele = driver.find_element_by_name(value)
            return css_ele
        elif  css == "class":
            css_ele = driver.find_element_by_class_name(value)
            return css_ele
        elif  css == "link_text":
            css_ele = driver.find_element_by_link_text(value)
            return css_ele
        elif  css == "xpath":
            css_ele = driver.find_element_by_xpath(value)
            return css_ele
        elif  css == "css":
            css_ele = driver.find_element_by_css(value)
            return css_ele
        else:
            return False
            #raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")


    #find_elements_by_的用法
    def by_elements(self, css, value):
        if css == "id":
            css_ele = driver.find_elements_by_id(value)
            return css_ele
        elif  css == "class":
            css_ele = driver.find_elements_by_class_name(value)
            return css_ele
        elif  css == "name":
            css_ele = driver.find_elements_by_name(value)
            return css_ele
        elif  css == "link_text":
            css_ele = driver.find_elements_by_link_text(value)
            return css_ele
        elif  css == "xpath":
            css_ele = driver.find_elements_by_xpath(value)
            return css_ele
        elif  css == "css":
            css_ele = driver.find_elements_by_css_selector(value)
            return css_ele
        else:
            return False
            #raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")

    def colse_app(self):
        driver.close_app()

    #模拟点击物理键
    def click_keycode(self, kc):
        #action = TouchAction(driver)
        if kc == 4:
            driver.keyevent(kc)
        if kc == 3:
            driver.keyevent(kc)
        if kc == 82:
            driver.keyevent(kc)
        if kc == 66:
            driver.keyevent(kc)

    #启动应用
    def start_app(self):
        driver.launch_app()

    #关闭应用
    def close_app(self):
        driver.close_app()

    #手指向下一点点
    def swipeUp(self, t):
        # 获得屏幕大小宽和高
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        # 手指向上滑动
        x1 = int(x * 0.5)  #x坐标
        y1 = int(y * 0.75)   #起始y坐标
        y2 = int(y * 0.25)   #终点y坐标
        driver.swipe(x1, y1, x1, y2, t*1000)

    #截图功能
    def screen_shot(self):
        print "shot:123"
        #driver.save_screenshot('./result/image/1.png')
        driver.get_screenshot_as_file('./result/images/login.png')