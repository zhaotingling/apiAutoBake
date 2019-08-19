#coding=utf-8

# ****************************************************************************************
# Author     : ztl
# Version    : 1.0
# Date       : 2019.5.1
# Description: 获取用户的token，并返回token值。
# *****************************************************************************************

import requests
import json
from common.baseConf import baseconf
from function.comfunction import commenfuction
from time import sleep
from common.logger import Logger

logger = Logger(logger='GetAccessToken').getlog()

class GetAccessToken():

    def getUserToken(self, phone):
        url = "http://emc.ts.bakeroad.com/code/imageVerificationCode"
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        response0 = requests.get(url, headers=headers)
        re0 = json.loads(response0.cookies)
        tt = re0['imgToken']
        imgToken = "imgToken=" + tt

        loginurl = "http://emc.ts.bakeroad.com/dologin.so"
        headers1 = {'Accept':'application/json','Content-Type':'application/x-www-form-urlencoded','Accept-Encoding':'application/gzip',"Cookie":imgToken}
        body = {"logname": "admin@danlex", "logpwd": "111111aa","x":129}
        response = requests.post(loginurl, data=json.dumps(body),headers=headers1)
        re = json.loads(response.cookies)
        return re['sessionId']


    def apiopenApikey(self):
        sleep(1)
        paras = baseconf().get_prepareDateJson("basedata","data1")

        try:
            respon = commenfuction().loginuserfunction(paras)
            data = baseconf().loadsResponse(respon.text)
            if data['code'] == 200:
                logger.info(u"获取apikey正常，并返回")
                return data["result"]["apikey"]
            else:
                logger.info(u"获取apikey:code!=200")
                raise NameError("error")
        except Exception as e:
            print(u"获取apikey异常！")
            logger.info(u"获取apikey异常！")


