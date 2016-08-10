#!/usr/bin/evn python
#encoding:utf8
from multiprocessing import Process,Queue
import os,time,random

def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['chu','liu','wang']:
        print('%s process put %s to queue...' % (os.getpid(), value))
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get()
        print('%s process get %s from queue.' % (os.getpid(), value))

if __name__=='__main__':
    #父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    #启动子进程pw，写入
    pw.start()
    #启动子进程pr，读取
    pr.start()
    #等待pw结束
    pw.join()
    #pr进程里是死循环，无法等待其结束，只能强制终止
    pr.terminate()
