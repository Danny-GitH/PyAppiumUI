#!/usr/bin/env python
#coding:utf-8
__author__ = 'dingrui'
import sys
import smtplib
from Config_File import EmailConfig
from public_method.Zip_Log import zip_ya
import time
reload(sys)
#sys.setdefaultencoding('utf8')

from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
def send_Mail():
    try:
        w = EmailConfig.Smtp_Server
        smtp = smtplib.SMTP(EmailConfig.Smtp_Server, 25)
        sender = EmailConfig.Smtp_Sender
        password = EmailConfig.Smtp_Sender_Password
        receiver = EmailConfig.Smtp_Receiver
        smtp.login(sender, password)
        msg = MIMEMultipart()
        now = time.strftime("%Y-%m-%d-%H_%M_%S")
        # 编写html类型的邮件正文，MIMEtext()用于定义邮件正文
        # 发送正文
        text = MIMEText('你好！', 'text', 'utf-8')
        # 定义邮件正文标题
        text['Subject'] = Header('XXXXUI自动化测试报告', 'utf-8')
        text["Accept-Language"] = "zh-CN"
        text["Accept-Charset"] = "ISO-8859-1,utf-8"
        msg.attach(text)

        # ---这是附件部分---
        # zip类型附件，MIMEApplication不管什么类型都可以用

        zip_pathname = zip_ya()
        part = MIMEApplication(open(zip_pathname, 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=zip_pathname)
        msg.attach(part)
        # 发送附件
        # Header()用于定义邮件主题，主题加上时间，是为了防止主题重复，主题重复，发送太过频繁，邮件会发送不出去。
        msg['Subject'] = Header('[执行结果：' + 'XXXXUI自动化测试报告' + now, 'utf-8')
        # 定义发件人，如果不写，发件人为空
        msg['From'] = sender
        # 定义收件人，如果不写，收件人为空
        msg['To'] = ",".join(receiver)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        return True
    except smtplib.SMTPException as e:
        print e
        #return False

if __name__ == '__main__':
    send_Mail()
