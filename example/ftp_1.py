#!/usr/bin/env python
#encoding:utf8

from ftplib import FTP

def ftpconnect():
    ftp_server = 'v1.ftp.upyun.com'
    username = 'dev/iotekimg'
    password = 'iotek_dev'
    ftp = FTP()
#    ftp.set_debuglevel(2)  #打开调试级别2，显示详细信息
    ftp.connect(ftp_server,21)
    ftp.login(username,password)
    return ftp

def downloadfile():
    remotepath = "/test/123.png"
    ftp = ftpconnect()
    print ftp.getwelcome()
    bufsize = 1024
    localpath = '/tmp/123.png'
    fp = open(localpath,'wb')
    ftp.retrbinary('RETR ' + remotepath,fp.write,bufsize)
    fp.close()
    ftp.quit()

def uploadfile():
    remotepath = '/test/345.png'
    ftp = ftpconnect()
    bufsize = 1024
    localpath = '/tmp/345.png'
    fp = open(localpath,'rb')
    ftp.storbinary('STOR '+ remotepath ,fp,bufsize)
    fp.close()
    ftp.quit()

ftp = ftpconnect()
#a = ftp.retrlines('LIST')
a = ftp.dir('/test')
print type(a)
print list(a)
#downloadfile()
#uploadfile()
