#!/usr/bin/python
# -*- coding= utf-8 -*-

# ****************************************************************************************
# Author     : ztl
# Version    : 1.0
# Date       : 2019.5.1
# Description: 基础包：接口请求方法的封装
# *****************************************************************************************

import requests
import json
from common.logger import Logger
import os.path


logger = Logger(logger='WebRequests').getlog()


class Webrequests:

    def get(self,url,para,headers):
        '''

        :param url:
        :param para:
        :param headers:
        :return:
        '''
        try:
            r = requests.get(url,params=para,headers=headers)
            logger.info(u"获取返回值")
            return r
        except BaseException as e:
            print(u"请求失败！",str(e))
            logger.error("WebRequests:error")

    def get_noHeader(self, url, para):
        try:
            r = requests.get(url,params=para)
            logger.info(u"获取返回值")
            return r
        except BaseException as e:
            print(u"请求失败！", str(e))
            logger.error("WebRequests:error")

    def get_noPara(self,url,headers):
        try:
            r = requests.get(url,headers=headers)
            logger.info(u"获取返回值")
            return r
        except BaseException as e:
            print(u"请求失败！",str(e))
            logger.error("WebRequests:error")

    def get_url(self,url):
        try:
            r = requests.get(url)
            logger.info(u"获取返回值")
            return r
        except BaseException as e:
            print(u"请求失败！",str(e))
            logger.error("WebRequests:error")



    def post(self,url,para,headers):
        try:
            r = requests.post(url,data=para,headers=headers)
            logger.info(u"post接口:获取返回值")
            return r
        except BaseException as e:
            logger.error("WebRequests:error")
            print(u"请求失败！",str(e))

    def post_noHeader(self,url,para):
        try:
            r = requests.post(url,data=para)
            logger.info(u"post接口:获取返回值")
            return r
        except BaseException as e:
            logger.error("WebRequests:error")
            print(u"请求失败！",str(e))

    def post_json(self,url,para,headers):
        try:
            data0 = para
            data = json.dumps(data0)
            r = requests.post(url,data=data,headers=headers)
            print(u"获取返回的状态码", r.status_code)
            return r
        except BaseException as e:
            logger.error("WebRequests:error")
            print(u"请求失败！",str(e))

    def post_json_noHeader(self,url,para):
        try:
            data0 = para
            data = json.dumps(data0)
            r = requests.post(url,data=data)
            print(u"获取返回的状态码", r.status_code)
            return r
        except BaseException as e:
            logger.error("WebRequests:error")
            print(u"请求失败！",str(e))

    def delete(self,url,para,headers):
        try:
            r = requests.delete(url,data=para,headers=headers)
            print(u"获取返回的状态码", r.status_code)
            return r.status_code
        except BaseException as e:
            logger.error("WebRequests:error")
            print(u"请求失败！", str(e))

    def delete_noHeader(self,url,para):
        try:
            r = requests.delete(url,data=para)
            print(u"获取返回的状态码", r.status_code)
            return r.status_code
        except BaseException as e:
            logger.error("WebRequests:error")
            print(u"请求失败！", str(e))

    def delete_noPara(self,url,headers):
        try:
            r = requests.delete(url,headers=headers)
            print(u"获取返回的状态码", r.status_code)
            return r.status_code
        except BaseException as e:
            logger.error("WebRequests:error")
            print(u"请求失败！", str(e))

    def delete_url(self,url):
        try:
            r = requests.delete(url)
            print(u"获取返回的状态码", r.status_code)
            return r.status_code
        except BaseException as e:
            logger.error("WebRequests:error")
            print(u"请求失败！", str(e))

    def put(self,url,para,headers):
        try:
            r = requests.put(url,data=para,headers=headers)
            print(u"获取返回的状态码", r.status_code)
            return r
        except BaseException as e:
            logger.error("WebRequests:error")
            print(u"请求失败！",str(e))
