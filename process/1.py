#!/usr/bin/evn python
#encoding:utf8
import os

print('Process (%s) start...' % os.getpid())
#创建一个子进程
pid = os.fork()
if pid == 0:
    print('I am child process %s and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
