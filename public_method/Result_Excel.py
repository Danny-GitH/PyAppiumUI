#!/usr/bin/env python
#coding:utf-8
__author__ = 'dingrui'
import os
from public_method.Read_Excel import *
from Config_File.CommPath import ConnPath

# 获取config中的config.ini公用参数

Obj = ConnPath()
config = Obj.Conf_Path()
path = config.get("get_path", "path")

def readFilename(path):
    for root, dirs, files in os.walk(path):
        return root, dirs, files

def startfind_count(root, dirs, files):
    j = 0
    count = []
    for ii in files:
        if ii.startswith('Demo_') and ii.endswith('.py'):
            j = j + 1
            count.append(j)
        else:
            continue
    return count

def startfind(root, dirs, files):
    book, wb, wt = read_excel()
    i = 0
    for ii in files:
        if ii.startswith('Demo_') and ii.endswith('.py'):
            case_Name = ii.split('.py')[0]
            i = i + 1
            wt.write(i, 0, case_Name)
        else:
            continue

    wb.save(excel_Name)
