#!/usr/bin/env python
import paramiko

f_s = file('/tmp/test')
f_d = file('/tmp/test1','a')
line_s = f_s.readlines()
for line in line_s:
    if 'root' not in line:
        f_d.write(str(line))
f_s.close()
f_d.close()



user = 'root'
host_list = ['192.168.8.221','192.168.8.223','192.168.8.224']
pkey_file = '/root/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(pkey_file)

for host in host_list:
     t = paramiko.Transport((host,22))
     t.connect(username=user,pkey=key)
     sftp = paramiko.SFTPClient.from_transport(t)
     sftp.put('/tmp/test1','/tmp/test')
     t.close()
