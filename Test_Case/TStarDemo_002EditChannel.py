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

class Conn_2(unittest.TestCase):
    def setUp(self, name = os.path.basename(__file__)):
        self.name = name
        obj = script_name(self.name)
        #获取log记录对象
        self.mylogger = Logger(logger= __name__, logname = obj.ScriptName())
        self.mylogger.getlog().info(u"驱动加载成功")
        PySelenuim().start_app()

    def test_search_in(self):
        try:
            #首次启动信息流sdk，检查进入通用demo页面
            self.start_sdk_comm_button = PySelenuim().by_element("id","com.startnews.demo:id/bt_custom_demo")
            #获取该元素的文本值
            start_sdk_comm_button_text = self.start_sdk_comm_button.get_attribute("text")
            self.mylogger.getlog().info(u"进入通用demo页面成功...")
        except Exception as e:
            self.mylogger.getlog().info(u"进入通用demo页面失败...%s",e)
            raise Exception(u"进入通用demo页面失败...%s",e)
        self.assertEqual((start_sdk_comm_button_text), u'通  用demo')

        try:
            #点击进入启动通用版demo页
            self.start_sdk_comm_button.click()
            #首次启动信息流sdk，检查进入宿主配置页面
            self.start_sdk_button = PySelenuim().by_element("id","com.startnews.demo:id/start_news")
            #点击启动，进入demo资讯首页
            self.start_sdk_button.click()
            #点击添加频道按钮进入频道编辑页面
            Click_Edit_Channel = PySelenuim().by_element("id","com.startnews.plugin:id/channel_add_iv")
            Click_Edit_Channel.click()
            #获取频道编辑文本值
            Edit_Value = driver.find_element_by_id("com.startnews.plugin:id/edit_mode_tv").get_attribute("text")
            print "Edit_Value:" + Edit_Value
            self.mylogger.getlog().info(u"进入频道编辑页面成功！")
        except Exception as e:
            print e
            self.mylogger.getlog().info(u"进入频道编辑页面失败！")
            raise AssertionError(u"进入频道编辑页面失败！")
        self.assertEqual(Edit_Value, "编辑")

        try:
            #点击按钮，由“编辑”变为“完成”
            Click_Edit = PySelenuim().by_element("id", "com.startnews.plugin:id/edit_mode_tv")
            Click_Edit.click()
            Success_Value = PySelenuim().by_element_dr("id","com.startnews.plugin:id/edit_mode_tv").get_attribute("text")
            self.mylogger.getlog().info(u"编辑字样变为完成字样成功，测试通过！")
        except Exception as e:
            print e
            self.mylogger.getlog().info(u"编辑字样变为完成字样失败，测试不通过！")
            raise AssertionError(u"编辑字样变为完成字样失败，测试不通过！")

        self.assertEqual(Success_Value, u"完成")

        try:
            #点击添加频道
            Add_Channel = PySelenuim().by_elements("id","com.startnews.plugin:id/text_item")
            Add_Channel[-1].click()
            #关闭编辑页面，进入首页
            Close_Window = PySelenuim().by_element_dr("id","com.startnews.plugin:id/close_windows_btn")
            Close_Window.click()
            PySelenuim().by_element("id","com.startnews.plugin:id/channel_add_iv")
            self.mylogger.getlog().info(u"关闭窗口成功，进入列表页")
            return True
        except Exception as e:
            self.mylogger.getlog().info(u"关闭窗口进入列表页失败")
            raise AssertionError(u"关闭窗口进入列表页失败")


    def tearDown(self):
        # 驱动
        # wait = WebDriverWait(self.driver, 30)
        # 清除测试数据，还原测试前的环境
        time.sleep(5)
        PySelenuim().close_app()
        PySelenuim().close_app()
        self.mylogger.getlog().info(u"该测试用例结束，关闭应用！\n")
        #获取日志正文信息，写入到email中
        log_name = self.mylogger.log_name
        f = open(log_name, 'rb')
        # 读取测试报告正文
        #mail_body = f.readlines()
        f.close()
        #send_Mail(self, mail_body)

if __name__ == "__main__":
    unittest.main()
