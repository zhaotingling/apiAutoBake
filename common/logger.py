# -*- coding: utf-8 -*-

# ****************************************************************************************
# Author     : ztl
# Version    : 1.0
# Date       : 2019.5.1
# Description: 操作日志方法封装，方便调制脚本。
# *****************************************************************************************

import logging
import os.path
import time


class Logger(object):

    def __init__(self, logger):
        '''''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''

        # 创建一个logger，初始化类
        self.logger = logging.getLogger(logger)

        # 这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志，防止重复打日志
        if not self.logger.handlers:
            #设置日志级别，debug,info,error,warnong,critical
            self.logger.setLevel(logging.DEBUG)

         # 创建一个handler，用于写入日志文件
            now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            log_path = os.path.abspath('.')
            log_name = log_path.split('apiAutoBake')[0] + "apiAutoBake\\logs\\test"  + now + '.log'

            fh = logging.FileHandler(log_name)
            fh.setLevel(logging.INFO)

         # 再创建一个handler（句柄），用于输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # 定义handler的输出格式
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # 给logger添加handler（句柄）
            self.logger.addHandler(ch)
            self.logger.addHandler(fh)
            # 控制台只显示结果不显示操作日志
            # self.logger.removeHandler(ch)



    def getlog(self):
        return self.logger