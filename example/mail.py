#!/usr/bin/env python
#encoding:utf8
#导入 smtplib 和MIMETest
import smtplib
from email.mime.text import MIMEText

mailto_list = ['chu0306@126.com','717141697@qq.com']

mail_name = "储昭洪"
mail_host = 'smtp.ym.163.com'
mail_user = 'zh.chu@haitongwangxiao.com'
mail_pass = 'chu0306'

def send_mail(to_list, sub):
    me = mail_name + "<"+mail_user+">"
    content = "测试邮件"
    msg = MIMEText(content,_charset="utf-8")
    msg['Sbuject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
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

if send_mail(mailto_list,"标题"):      
    print "测试成功"
else:
    print "测试失败"
