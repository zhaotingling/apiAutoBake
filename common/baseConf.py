#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ****************************************************************************************
# 基础包：配置服务
# Author     : ztl
# Version    : 1.0
# Date       : 2019.5.1
# Description: 配置文件的读取、区片化字符串、返回响应值反序列方法封装。
# *****************************************************************************************

import ConfigParser
import os
import json

config = ConfigParser.ConfigParser()

class baseconf(object):

    def get_prepareDate(self,title, key):
        """
            #     参数配置，读取配置文件config.ini中的数据
            #     :param title: 配置文件的头信息
            #     :param key: 配置文件的key值
            #     :return: 配置文件的value
        """
        # report_path = os.path.join(os.getcwd(), "conf") + '/configs.ini'
        # report_name = os.path.realpath("bakeApiAutoTest") + "\\conf\\configs.ini"
        path = os.path.abspath('.')
        report_name = path.split("apiAutoBake")[0] +"apiAutoBake\\conf\\configs.ini"

        try:
            config.read(report_name)
            value = config.get(title, key)
            return value
        except BaseException as e:
            print(u"获取参数失败 %s" % e)

    def get_prepareDateJson(self,title, key):
        """
            #     参数配置，读取配置文件config.ini中的数据，内容为Json格式时
            #     :param title: 配置文件的头信息
            #     :param key: 配置文件的key值
            #     :return: 配置文件的value
        """
        path = os.path.abspath('.')
        report_path = path.split("apiAutoBake")[0] + "apiAutoBake\\conf\\configs.ini"

        try:
            config.read(report_path)
            value0 = config.get(title, key)
            value = json.loads(value0)
            return value
        except BaseException as e:
            print(u"获取参数失败 %s" % e)

    def get_title_list(self):
        """
        获取所有title
        :return: title list
        """
        try:
            title = config.sections()
            return str(title).decode("string_escape")
        except Exception, e:
            print ("获取title信息失败 %s", e)



# 将 字符串 转化成 list
    def strdataSetLeft(self,strdata):
        """
        将response为字符串时，去除头部的["
        :return: 字符串
        """
        try:
            res = strdata.strip('["')
            return res
        except BaseException as e:
            print(u"去除字符串的头部的中括号和双引号失败 %s" ,e)

    def strdataSetRigh(self,strdata):
        """
        将response为字符串时，去除尾部的"]
        :return: 字符串
        """
        data = baseconf().strdataSetLeft(strdata)
        try:
            res = data.strip('"]')
            return res
        except BaseException as e:
            print(u"去除字符串的末尾的中括号和双引号失败 %s" ,e)

    def strTolist(self,strdata):
        """
        将response为字符串时，去除头尾的特殊字符，区片化转化成list
        :return: list
        """
        data = baseconf().strdataSetRigh(strdata)
        try:
            res = data.split('","')
            return res
        except Exception as e:
            print(u"区片化字符串失败 %s",e)


# 将json对象转成原生对象，当response为str时，反序列化转换成dict
    def loadsResponse(self,respon):
        try:
            res = json.loads(respon)
            return res
        except Exception as e:
            print(u" JSON 字符串解码为 Python 对象失败 %s",e)









