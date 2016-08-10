#!/usr/bin/evn python
#enconding:utf8
from multiprocessing import Pool
import os
import time

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    time.sleep(10)

if __name__=='__main__':
    print('parent process %s.' % os.getpid())
    name_list = ['chu','liu','wang','huang']
    p = Pool(5)
    for i in name_list:
        p.apply_async(run_proc, args=(i,))
    print('Child process will start.')
    p.close()
    p.join()
    print('Child process end.')
