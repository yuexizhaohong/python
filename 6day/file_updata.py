#!/usr/bin/evn python

f_s = file('/tmp/test')
f_d = file('/tmp/test1','a')
line_s = f_s.readlines()
for line in line_s:
    if 'root' not in line:
        f_d.write(str(line))
f_s.close()
f_d.close()
