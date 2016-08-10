#user/bin/python
#coding:utf-8

import dns.resolver
domain=raw_input('Please input an domain:')
A=dns.resolver.query(domain,'A')
print A.response.answer
for i in A.response.answer:
    for j in i.items:
        print j.address
