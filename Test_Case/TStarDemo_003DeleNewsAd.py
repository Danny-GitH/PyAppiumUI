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

class Conn_3(unittest.TestCase):
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
            #点击进入娱乐频道，获取列表新闻
            self.channel_names = PySelenuim().by_elements("id","com.startnews.plugin:id/channel_name")
            self.channel_names[2].click()
            time.sleep(5)
            channel_name_3 = self.channel_names[2].get_attribute("text")
            self.mylogger.getlog().info(channel_name_3)
            print(unicode(channel_name_3))
            self.mylogger.getlog().info("获取娱乐频道成功！")
        except Exception as e:
            print e
            self.mylogger.getlog().info("获取娱乐频道失败，请检查对应的频道是否是娱乐频道！")
            raise Exception("获取娱乐频道失败，请检查对应的频道是否是娱乐频道！...%s",e)
        #断言当前频道是否是娱乐频道
        self.assertEqual(channel_name_3, u"娱乐")

        try:
            #点击新闻列表的任意一条新闻的删除按钮
            self.unlike_button = PySelenuim().by_elements("id", "com.startnews.plugin:id/img_unlike")
            self.unlike_button[1].click()
            #选择任意一个理由确认删除
            self.delete_reasons = PySelenuim().by_elements("id", "com.startnews.plugin:id/tv_content")
            self.delete_reasons[2].click()
            time.sleep(1)
            self.mylogger.getlog().info("删除娱乐频道的垃圾资讯成功！")
            return True
        except Exception as e:
            self.mylogger.getlog().info("删除娱乐频道的垃圾资讯失败！")
            raise Exception("删除娱乐频道的垃圾资讯失败！...%s",e)

    def tearDown(self):
        # 驱动
        # wait = WebDriverWait(self.driver, 30)
        # 清除测试数据，还原测试前的环境
        time.sleep(5)
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
