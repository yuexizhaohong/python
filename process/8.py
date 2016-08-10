#!/usr/bin/evn python
#enconding:utf8
import threading

#local_school = threading.local()
std = 0
student = 0

def process_student():
#    std = local_school.student
    std = student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
#    local_school.student = name
    student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
