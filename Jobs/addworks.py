# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 21:37:19 2022

@author: 大班
"""

import db02

items = input("工作項目名稱:")
info = input("工作內容:")
employeeid = input("負責該項目員工id:")

sql = "insert into works(items,info,employeeid) values('{}','{}','{}') ".format(items,info,employeeid)


cursor = db02.conn.cursor()

cursor.execute(sql)

db02.conn.commit()

db02.conn.close()