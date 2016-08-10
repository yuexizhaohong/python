#!/usr/bin/evn python
import paramiko

host = '192.168.8.223'
user = 'root'

pkey_file = '/root/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(pkey_file)

t = paramiko.Transport((host,22))
t.connect(username=user,pkey=key)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put('/tmp/test','/tmp/test2')
t.close()
