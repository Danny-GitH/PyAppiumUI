#!/usr/bin/env python
#coding:utf-8
__author__ = 'dingrui'
import time
import xlrd
import xlwt
from xlutils.copy import copy

rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
excel_Name = "D:\APPNUIM" + rq + ".xls"
def new_excel():
    wt = xlwt.Workbook()
    ws_1 = wt.add_sheet('Test_Record'.decode("utf-8"))
    first_col = ws_1.col(0)
    four_col = ws_1.col(4)
    six_col = ws_1.col(6)
    first_col.width = 300 * 20
    four_col.width = 300 * 40
    six_col.width = 1000 * 20
    ws_1.write(0, 0, 'Case_Name')
    ws_1.write(0, 2, 'Result')
    ws_1.write(0, 4, 'Cause')
    ws_1.write(0, 6, 'Log_Path')

    ws_2 = wt.add_sheet("results".decode("utf-8"))
    ws_2.write(0, 0, "case_sum")
    ws_2.write(0, 1, "fail_num")
    ws_2.write(0, 2, "pass_num")
    ws_2.write(0, 3, "rate")
    wt.save(excel_Name)
    #return wt, ws_1

def read_excel():
    # 打开指定路径中的xls文件，得到book对象
    #xls_file = "D:\Case_Traces_1.xls"
    book = xlrd.open_workbook(excel_Name, formatting_info=True)  # 得到Excel文件的book对象，实例化对象
    wb = copy(book)
    wt = wb.get_sheet(0)
    return book, wb, wt