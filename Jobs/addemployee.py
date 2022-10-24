# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 11:09:50 2022

@author: 大班
"""

import db02

name = input("請輸入員工名稱:")
sex = input("性別(F/M):")
tel = input("請輸入電話:")
assume = input("正式上班時間:yyyy-mm-dd:")


sql = "insert into employee(name,sex,tel,assume) values('{}','{}','{}','{}')".format(name,sex,tel,assume)

cursor = db02.conn.cursor()

cursor.execute(sql)

db02.conn.commit()

updata = input("是否修改資料(y/n):")
if updata =="y":
    
    sql = "select id from employee"
    
    cursor = db02.conn.cursor()

    cursor.execute(sql)

    db02.conn.commit()
    
    result = cursor.fetchall()
    print("員工id及姓名")
    for row in result:
        print(row[0],row[1])
    
    no = input("欲修改的員工id:")
    revise = input("請輸入欲修改電話:")
    revise2 = input("請輸入欲修改的性別(F/M):")
    
    sql = "update employee set tel='{}' , sex='{}' where id='{}'".format(revise,revise2,no)
    
    cursor.execute(sql)
    db02.conn.commit()
else:
    db02.conn.close()