# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 22:52:44 2022

@author: 大班
"""

import db02
from datetime import datetime

def addemployee(name,sex,tel):
    now = datetime.now()
    today = datetime.strftime(now,'%Y-%m-%d')
    sql = "insert into employee(name,sex,tel,assume) values('{}','{}','{}','{}')".format(name,sex,tel,today)
    
    cursor = db02.conn.cursor()
    cursor.execute(sql)
    db02.conn.commit()
    
def addworks(employeeid,items,info):
    sql = "insert into works(items,info,employeeid) values('{}','{}','{}')".format(items,info,employeeid)
    
    cursor = db02.conn.cursor()
    cursor.execute(sql)
    db02.conn.commit()
    
def allemployee():
    sql = "sqlect id,name from employee"
    cursor = db02.conn.cursor()
    cursor.execute(sql)
    db02.conn.commit()
    result = cursor.fetchall()
    for row in result:
        print("員工編號:",row[0])
        print("員工姓名:",row[1])
        print()
        
def searchemployee(employeeid):
    sql = "sqlect id,name,sex,assume from employee where id='{}'".format(employeeid)
    cursor = db02.conn.cursor()
    cursor.execute(sql)
    db02.conn.commit()
    result = cursor.fetchall()
    for row in result:
        print("員工編號:",row[0])
        print("員工姓名:",row[1])
        print("員工姓別:",row[2])
        print("就職日:",row[3])
        print()
    else:
        print("沒有此員工")
        
def updateemployee(employeeid,tel,sex):
    sql = "update employee set tel='{}',sex='{}' where id='{}'".format(tel,sex,employeeid)
    cursor = db02.conn.cursor()
    cursor.execute(sql)
    db02.conn.commit()
    
def searchemployeeworks(employeeid):
    sql = "select employee.name,works.* from employee inner join works on employee.id = works.employeeid where employee.id='{}'".format(employeeid)
    cursor = db02.conn.cursor()
    cursor.execute(sql)
    db02.conn.commit()
        
    result = cursor.fetchall()
    for row in result():
        print("員工:",row[0])
        print("工作項目:",row[2])
        print("工作內容:",row[3])
        print()
        
if __name__ == "__hw__":
    while True:
        
        item = input("員工系統:a->新增員工 w->新增員工工作 q->查詢 u->修改 e->員工工作內容 x->離開:")
    
        if item == "x":
            break
        elif item == "a":
            name = input("新增員工姓名:")
            sex = input("性別(F/M):")
            tel = input("電話:")
            addemployee(name,sex,tel)
            allemployee()
        elif item == "w":
            allemployee()
            empid = input("請輸入員工編號:")
            items = input("請輸入工作事項:")
            info = input("請輸入內容:")
            addworks(empid,items,info)
        elif item == "q":
            eid = input("請輸入員工編號:")
            searchemployee(eid)
        elif item == "u":
            allemployee()
        
            eid = input("請輸入員工編號:")
            tel = input("請輸入修改的電話:")
            sex = input("請輸入修改的性別(F/M):")
            updateemployee(eid, tel, sex)
        elif item == "e":
            employeeid = input("請輸入員工編號:")
            searchemployeeworks(employeeid)
    
    
    
        
