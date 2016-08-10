#!/usr/bin/env python
import paramiko
import threading

host_list = ['192.168.8.221','192.168.8.223','192.168.8.224']
user = 'root'
pkey_file = '/root/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(pkey_file)

def run(host):
    t = paramiko.Transport((host,22))
    t.connect(username=user,pkey=key)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put('/tmp/test','/tmp/test11')
    t.close()

for host in host_list:
    s = threading.Thread(target=run,args=(host,))
    s.start()


