#!/usr/bin/env python
# coding:utf-8
__author__ = 'dingrui'
import time
import re
import sys
import unittest
reload(sys)
sys.setdefaultencoding('utf8')
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
from public_method.Get_script_name import *
from public_method.Screen_Shot import *


class Conn_1(unittest.TestCase):
    def setUp(self, name = os.path.basename(__file__)):
        self.name = name
        obj = script_name(self.name)
        self.ScriptName = obj.ScriptName()
        #获取log记录对象
        self.mylogger = Logger(logger= __name__, logname = obj.ScriptName())
        PySelenuim().start_app()
        self.mylogger.getlog().info("驱动加载成功")

    def test_search_in(self):
        try:
            #首次启动信息流sdk，检查进入通用demo页面
            self.start_sdk_comm_button = PySelenuim().by_element("id","com.startnews.demo:id/bt_custom_demo")
            #获取该元素的文本值
            start_sdk_comm_button_text = self.start_sdk_comm_button.get_attribute("text")
            self.mylogger.getlog().info(u"进入通用demo页面成功...")
            screen_shot(self.ScriptName).Screenshot1()
        except Exception as e:
            self.mylogger.getlog().info(u"进入通用demo页面失败...%s",e)
            raise Exception(u"进入通用demo页面失败...%s",e)
        self.assertEqual((start_sdk_comm_button_text), u'通  用demo')

        try:
            #点击进入启动通用版demo页
            self.start_sdk_comm_button.click()
            #首次启动信息流sdk，检查进入宿主配置页面
            self.start_sdk_button = PySelenuim().by_element("id","com.startnews.demo:id/start_news")
            #获取该元素的文本值
            start_sdk_button_text = self.start_sdk_button.get_attribute("text")
            self.mylogger.getlog().info(u"启动信息流sdk进入宿主配置页面成功")
        except Exception as e:
            self.mylogger.getlog().info(u"启动信息流sdk进入宿主配置页面失败...%s",e)
            raise Exception(u"启动信息流sdk进入宿主配置页面失败...%s",e)
        self.assertEqual((start_sdk_button_text), u'启动信息流')

        try:
            #点击启动，进入demo资讯首页
            self.start_sdk_button.click()
            self.firstpage_tuijian = PySelenuim().by_elements("id","com.startnews.plugin:id/channel_name")
            firstpage_tuijian_text = self.firstpage_tuijian[0].get_attribute("text")
            print "firstpage_tuijian_text: " + firstpage_tuijian_text
        except Exception as e:
            print e
            self.mylogger.getlog().info(u"启动信息流sdk进入首页资讯失败！")

            return False

        self.assertEqual(firstpage_tuijian_text, u'推荐')

    def tearDown(self):
        # 驱动
        # wait = WebDriverWait(self.driver, 30)
        # 清除测试数据，还原测试前的环境
        time.sleep(5)
        PySelenuim().close_app()
        PySelenuim().close_app()
        self.mylogger.getlog().info("该测试用例结束，关闭应用！\n")
        #获取日志正文信息，写入到email中
        log_name = self.mylogger.log_name
        f = open(log_name, 'rb')
        # 读取测试报告正文
        #mail_body = f.readlines()
        f.close()
        #send_Mail(self, mail_body)

if __name__ == "__main__":
    unittest.main()
