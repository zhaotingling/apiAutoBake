#coding=utf-8
# ****************************************************************************************
# Author     : ztl
# Version    : 1.0
# Date       : 2019.5.1
# Description: 接口请求方法，对每一个接口的请求进行单独设置，并将响应值进行返回。
# *****************************************************************************************

import requests
import json
import unittest
from time import sleep
from common.logger import Logger
from common.baseConf import baseconf
from common.WebRequests import Webrequests

logger = Logger(logger='commenfuction').getlog()


class commenfuction(object):

    def __init__(self):
        self.host = baseconf().get_prepareDate("basedata", "host")
        self.poshost = baseconf().get_prepareDate("basedata", "poshost")
        self.header = {'cache-control': "no-cache"}
        self.header3 = baseconf().get_prepareDateJson("headerdata","headers3")



    def aaafunction(self,param):

        url = self.host + '/v2/book/26718687?'
        re = Webrequests().get(url,param,self.header)
        return re


        # try:
        #     re = requests.get(url,data=param,headers=self.header)
        #     return re
        # except BaseException as e:
        #     print(u"报错了！接口异常，请注意检查")
        #     logger.info("aaafunction:error")


    def test02function(self):
        url = self.host + '/getAllUrl'
        re = Webrequests().get_noPara(url,self.header)
        return re


    def loginuserfunction(self,param):
        host = str(self.host)
        url = host + "/developerLogin?"
        re = Webrequests().post(url,param,self.header)
        return re

    def getFeedbakefunction(self,param):
        host = str(self.host)
        url = host + "/getFeedback?"
        re = Webrequests().post(url, param, self.header)
        return re

    def checkMaterialStorefunction(self,param):
        host = str(self.poshost)
        url = host + "/materialStoreInfo/checkMaterialStore?"
        try:
            re = Webrequests().post(url,param,self.header)
            logger.info(u"function方法调用：正常")
            return re
        except Exception as e:
            logger.info(u"function方法：异常")
            logger.error(str(e))
            print(u"function方法：异常")

    def userFeedbackfunction(self,param):
        host = str(self.host)
        url = host + "/userFeedback?"
        try:
            re = Webrequests().post(url,param,self.header3)
            return re
        except Exception as e:
            print("error")













