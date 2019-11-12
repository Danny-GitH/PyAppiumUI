#!/usr/bin/env python
#coding:utf-8
__author__ = 'dingrui'
import logging
import os
import time
from public_method.Log_Method import Logger
from public_method.Get_script_name import *

#导入截图模
from PIL import ImageGrab

class screen_shot(object):
    def __init__(self,name):
        self.scriptfilename = name

    def Screenshot1(self):
        filePath = os.path.split(os.path.dirname(__file__))[0]
        img_folder = os.defpath(filePath +'/result/image/'+ '\\' + self.scriptfilename)
        print (img_folder)
        rq = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
        # log文件的存放路径
        imPath = filePath + '/result/image/' + self.scriptfilename + '/' + rq + '.png'
        print "imPath: " + imPath
        im = ImageGrab.grab()
        im.save(imPath)

#if __name__ == "__mian__":
#    sc_shot = screen_shot("name")
#    config = sc_shot.Screenshot1()
