#!/usr/bin/env python
# coding:utf-8
__author__ = 'dingrui'
import ConfigParser
import os

class ConnPath(object):
    ''' Run test '''

    def __init__(self,conf_name = "SdkInfo.ini",name=''):
        self.conf_name = conf_name
        self.scriptname = name

    def Conf_Path(self):
        # 获取config中的config.ini公用参数
        config = ConfigParser.ConfigParser()
        proDir = os.path.split(os.path.realpath(__file__))[0]
        # proDir = os.path.dirname(os.path.realpath(__file__))  与上面一行代码作用一样
        configPath = os.path.join(proDir, self.conf_name)
        path = os.path.abspath(configPath)
        config.read(path)
        return config


if __name__ == '__main__':
    connpath = ConnPath()
    config = connpath.Conf_Path()