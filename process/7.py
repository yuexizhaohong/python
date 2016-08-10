#!/usr/bin/env python
#encoding:utf8
import time, threading

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance 
    balance = balance + n
    balance = balance - n

#每个循环都会加锁和释放锁，开销比较大
#def run_thread(n):
#    for i in range(100000):
#        lock.acquire()
#        try:
#            change_it(n)
#        finally:
#            lock.release()
#将每个线程加锁，只需要加锁两次
def run_thread(n):
    lock.acquire()
    try:
        for i in range(100000):
            change_it(n)
    finally:
        lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

