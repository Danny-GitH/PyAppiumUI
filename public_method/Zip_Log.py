#!/usr/bin/env python
#coding:utf-8
__author__ = 'dingrui'

import os
import zipfile
import time
def zip_ya():
    startdir = "D:\\Project\\Python_Appium_beta3\\Log\\"  #要压缩的文件夹路径
    print "startdir:" + startdir
    nowdate = time.strftime("%Y-%m-%d-%H_%M_%S")
    file_news = startdir + nowdate + '.zip' # 压缩后文件夹的名字
    print "file_news:" + file_news
    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED) #参数一：文件夹名
    zip_pathname = z.filename

    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir, '') #这一句很重要，不replace的话，就从根目录开始复制
        fpath = fpath and fpath + os.sep or ''#这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath+filename)
    z.close()
    return zip_pathname
