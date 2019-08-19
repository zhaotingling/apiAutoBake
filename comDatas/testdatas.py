#coding=utf-8

# ****************************************************************************************
# Author     : ztl
# Version    : 1.0
# Date       : 2019.5.1
# Description: 初始化接口的入参，对每个接口的入参定义一个入参方法，方便在case中使用
# *****************************************************************************************

class testData(object):

    def checkMaterialStockData(self):
        datas = {"materialId": "", "quantity": "", "isAutoProduct": ""}
        return datas


    def test02Data(self):
        datas = {"apikey":"", "page":"", "count":""}
        return datas

    def test03Data(self):
        datas = {"apikey":"", "text":"", "email":""}
        return datas

    def test03Data1212(self):
        datas = {"apikey":"", "text":"", "email":""}
        return datas



