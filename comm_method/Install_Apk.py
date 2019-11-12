#!/usr/bin/env python
#coding:utf-8
import os
from appium import webdriver

# 获取当前项目的根路径
apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

desired_caps ={}
# 设备系统
desired_caps['platformName'] = 'Android'

# 设备系统版本
desired_caps['platformVersion'] = '8.0.0'

# 设备名称
desired_caps['deviceName'] = 'HWLND-Q'

desired_caps['noReset'] = 'True'

# 测试apk包的路径
desired_caps['app'] = apk_path + '\\APP\\app-release.apk'

# 启动app
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
