#coding=utf-8
# ****************************************************************************************
# Author     : ztl
# Version    : 1.0
# Date       : 2019.5.1
# Description: 运行 testcase 文件夹下所有以test开头的.py ，且.py文件中的以test开头的case
# *****************************************************************************************

import unittest
import os
import HTMLTestRunner
import time
from common.SendEmail import sendEmail

# 用例路径
case_path = os.path.join(os.getcwd(),"testcase")


def all_case():
    discovers = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    return discovers


if __name__=="__main__":
    # 报告存放路径
    report_path = os.path.join(os.getcwd(), "test_report")
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

    HtmlFile = os.path.join(report_path,"report_"+now+".html")
    fp = file(HtmlFile, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'橙创烘焙云-API接口测试报告', description=u'用例测试情况')
    runner.run(all_case())
    fp.close()

    new_report = sendEmail().new_file(report_path)
    sendEmail().send_email(new_report)