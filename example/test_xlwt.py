#!/usr/bin/env python
#encoding:utf8

import xlwt

workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
sheet1.write(0,1,'aaaaaaaaaaaaaaaaaaa')
sheet1.write(3,2,'bbbbbbbbbbbbbbbbbbb')
workbook.save('/tmp/test.xls')
print 'sucess'
