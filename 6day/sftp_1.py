#!/usr/bin/evn python
import paramiko

host = '192.168.8.223'
user = 'root'
password = 'iotek123'

t = paramiko.Transport((host,22))
t.connect(username=user,password=password)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put('/tmp/test','/tmp/test1')
t.close()
