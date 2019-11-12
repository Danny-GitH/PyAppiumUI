#!/usr/bin/env python
# coding:utf-8
__author__ = 'dingrui'
import time
import re
import sys
import unittest
reload(sys)
#sys.setdefaultencoding('utf8')
from public_method.Log_Method import Logger
from public_method.Result_Excel import *
from public_method.Color_Change import *
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config_File.CommPath import ConnPath
from comm_method.Setup_app import Start_App_Para
from public_method.UI_Method import *
#导入截图模
from PIL import ImageGrab

class script_name(object):
    def __init__(self,name):
        self.scriptname = name
        # 获取当前脚本的名称
    def ScriptName(self):
        Xpath = self.scriptname.split(".")
        script_Name = Xpath[0]
        print("path_Name:",script_Name)
        return script_Name
