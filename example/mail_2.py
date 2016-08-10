#!/usr/bin/env python
#encoding:utf8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#创建一个带附件实例
msg = MIMEMultipart()
#邮件内容
txt = MIMEText("测试",'plain','utf8')
msg.attach(txt)
#构造附件
att = MIMEText(open('chu.html','rb').read(),'base64','gb2312')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment;filename="fujian"'
msg.attach(att)
#邮件头部
msg['to'] = '717141697@qq.com'
msg['from'] = 'zh.chu@haitongwangxiao.com'
msg['subject'] = 'hello'
#发送邮件
try:
    server = smtplib.SMTP()
    server.connect('smtp.ym.163.com')
    server.starttls()
    server.login('zh.chu@haitongwangxiao.com','chu0306')
    server.sendmail(msg['from'],msg['to'],msg.as_string())
    server.quit()
    print "发送成功"
except Exception,e:
    print str(e)
