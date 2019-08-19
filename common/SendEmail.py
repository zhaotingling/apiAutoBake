#coding=utf-8
import sys
# ***********************************************************************************
# Author     : ztl
# Version    : 1.0
# Date       : 2019.5.1
# Description: 获取最新的测试包高，并将测试报告发送到指定邮箱。
# 可参考：https://www.cnblogs.com/handaxing/p/6952293.html
# ************************************************************************************
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header



class sendEmail(object):


    def new_file(self,test_dir):
        # 获取最新的测试报告
        lists = os.listdir(test_dir)
        lists.sort(key=lambda fn: os.path.getmtime(test_dir + '\\' + fn))
        file_path = os.path.join(test_dir, lists[-1])
        return file_path

    # 3.定义：发送邮件，发送最新测试报告html
    def send_email(self,newfile):
        f = open(newfile, 'rb')
        mail_body = f.read()
        f.close()

        # smtpserver：发送邮箱服务器；发送邮箱用户名/密码：user/password；sender：发送者邮箱
        smtpserver = 'smtp.exmail.qq.com'
        user = 'zhaotingling@bakeroad.com'
        password = '990121Aa'
        sender = 'zhaotingling@bakeroad.com'
        # 接收邮箱，可设置多个接收邮箱，单个收件人的话，直接是receiver='XXX@163.com'
        receiver = ['zhaotingling@bakeroad.com']
        # 发送邮件主题
        subject = '自动化测试报告'
        # 编写 HTML类型的邮件正文
        msg = MIMEMultipart('mixed')
        msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
        msg.attach(msg_html1)
        msg_html = MIMEText(mail_body, 'html', 'utf-8')
        msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        msg.attach(msg_html)


        msg['From'] = 'zhaotingling@bakeroad.com'
        msg['To'] = ";".join(receiver)
        msg['Subject'] = Header(subject, 'utf-8')

        # 连接发送邮件
        try:
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver, 25)
            smtp.login(user, password)
            smtp.sendmail(sender, receiver, msg.as_string())
            smtp.quit()
        except Exception as e:
            print("Exceptioin",e)


