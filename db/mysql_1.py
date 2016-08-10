#!/usr/bin/env python
#encoding:utf8
import MySQLdb

sql_1 = "select * from tb_channel_user where create_user='21';"
mysql_db = MySQLdb.connect(host='192.168.8.53', user='iotek', passwd='iotek123', db='iotek_channel', port=3306)
mysql_cursor = mysql_db.cursor()
mysql_cursor.execute(sql_1)
data = mysql_cursor.fetchall()

for value in data:
    v = ','.join(str(v) for v in value)
    print v

