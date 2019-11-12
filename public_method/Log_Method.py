#!/usr/bin/env python
#coding:utf-8
__author__ = 'dingrui'
import logging
import os.path
import time
import sys



class Logger():

    def __init__(self, logger, logname):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        :param logger:
        """
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        log_path_excel = os.path.dirname(os.getcwd()) + '\\Log\\'
        print("log_path_excel:", log_path_excel)
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # 创建一个handler，用于写入日志文件
        file_case_name = log_path_excel + logname
        print("file_case_name:", file_case_name)
        os.mkdir(file_case_name, 0777)
        self.log_path = file_case_name
        log_path = self.log_path
        self.log_name = log_path + '/' + rq + logname + '.log'
        log_name = self.log_name
        fh = logging.FileHandler(log_name)

        #调高log等级
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # formatter = logging.Formatter( ("================================\n"
        #                                 "time:%(asctime)s\nlogger:%(name)s\nlevel:%(levelname)s\n"
        #                                 "file:%(filename)s\nfun:%(funcName)s\nlineno:%(lineno)d\n"
        #                                 "message:%(message)s" ))
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        fh.close()
        ch.close()

    def getlog(self):
        return self.logger
