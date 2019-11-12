#!/usr/bin/env python
# coding:utf-8
__author__ = 'dingrui'

from Config_File.CommPath import ConnPath

def Start_App_Para():
    # 获取config中的config.ini公用参数
    Obj = ConnPath()
    config = Obj.Conf_Path()
    platformName = config.get("news_demo", "platformName")
    appPackage = config.get("news_demo", "appPackage")
    appActivity = config.get("news_demo", "appActivity")
    #automationName = config.get("new_Info", "automationName")
    server='http://localhost:4723/wd/hub'
    #userid = config.get("login", "userid")
    #password = config.get("login", "password")
    # app启动参数
    desired_caps={
        "platformName": platformName,
        "deviceName": server,
        "appPackage": appPackage,
        "appActivity": appActivity,
        #"automationName":automationName,
        "noReset": "True"               # 启动app时不要清除app里的原有的数据
    }
    return server, desired_caps