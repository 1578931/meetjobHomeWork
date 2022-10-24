# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 20:20:19 2022

@author: 大班
"""

import db02

ids = input("請輸入欲查詢的該員工id:")

cursor = db02.conn.cursor()

sql2 = "select * from employee,works where employee.id = works.employeeid"

cursor.execute(sql2)

sql = "select employee.id , works.* from employee,works where employee.id = works.employeeid"

cursor.execute(sql)


result = cursor.fetchall()
print()
print("該員工負責的工作")
print()
for row in result:
    print(row[0],row[1],row[2],row[3],row[4])
    
  
db02.conn.close()