#!/usr/bin/evn python
#encoding:utf8
import subprocess, os

print('$ nslookup www.python.org')
print('parent pid is %s.'  % os.getpid())
r = subprocess.call(['nslookup', 'www.python.org'])
print('child pid is %s.' % os.getpid())
print('Exit code:', r)
