#!/usr/bin/env python
#coding:utf-8
__author__ = 'dingrui'

import os

def phoneInfo():
    device = os.popen('adb shell getprop ro.product.device').read()
    if device == '':
        print "没有获取到device，请检查测试机是否连接正常"
    else:
        return device
