#coding=utf-8
# ****************************************************************************************
# Author     : ztl
# Version    : 1.0
# Date       : 2019.5.1
# Description: 校验方法封装，对响应值进行校验。
# *****************************************************************************************

from common.logger import Logger

logger = Logger(logger='comVerify').getlog()


class comVerify(object):

    # def __init__(self,driver):
    #     self.driver = driver


    def TwoDataEqual(self,one,two,commen):
        if one == two:
            print(commen + u"：正常")
            logger.info(commen + u"：正常")
        else:
            logger.error(commen + u"：错误")
            print(commen + u"：错误")
            # raise NameError("error")

    def TwoDifferData(self,one,two,differ,commen):
        if one - two == differ:
            print(commen + u"：正常")
            logger.info(commen + u"：正常")
        else:
            print(commen + u"：错误")
            logger.error(commen + u"：错误")
            # raise NameError("error")

    def TwoDataAdd(self,one,two,sum,commen):
        if one + two == sum:
            print(commen + u"：正常")
            logger.info(commen + u"：正常")
        else:
            print(commen + u"：错误")
            logger.error(commen + u"：错误")
            # raise NameError("error")

    def OneInTwo(self,one,two,commen):
        if one in two:
            print(commen + u"：正常")
            logger.info(commen + u"：正常")
        else:
            print(commen + u"：错误")
            logger.error(commen + u"：错误")
            # raise NameError("error")

    def TwoDataUnEqual(self,one,two,commen):
        if one != two:
            print(commen + u"：正常")
            logger.info(commen + u"：正常")
        else:
            print(commen + u"：错误")
            logger.error(commen + u"：错误")
            # raise NameError("error")