#!/usr/bin/env python
#encoding:utf8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_mail(to_list, sub, filename):
    me = mail_name + "<"+mail_user+">"
    msg = MIMEMultipart()
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    submsg = MIMEBase('application', 'utf-8')
    submsg.set_payload(open(filename,'r').read())
    encoders.encode_base64(submsg)
    submsg.add_header('Content-Dispostition', 'attachment',filename='test')
    msg.attach(submsg)
    try:
        send_smtp = smtplib.SMTP()
        send_smtp.connect(mail_host)
        send_smtp.login(mail_user, mail_pass)
        send_smtp.sendmail(me, to_list, msg.as_string())
        send_smtp.close()
        return True
    except Exception, e:
        print str(e)
        return False

mail_host = 'smtp.ym.163.com'
mail_user = 'zh.chu@haitongwangxiao.com'
mail_pass = '********'
mail_name = '*****'
mailto_list = ['******@qq.com','*****@126.com']
title = 'check'
filename = "chu.html"
if send_mail(mailto_list,title,filename):
    print "发送成功"
else:
    print "发送失败" 
