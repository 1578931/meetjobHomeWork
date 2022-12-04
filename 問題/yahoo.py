# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 20:58:12 2022

@author: watson
"""

import requests
from bs4 import BeautifulSoup

import db

from datetime import datetime as dt # 抓日期函式庫

today = dt.today() # 抓今天的日期格式

todayS = today.strftime('%Y-%m-%d') # 將設定好的日期格式轉換為字串使用


url = "https://tw.buy.yahoo.com/search/product"

payload = {'p':'電視'}

data = requests.get(url,params=payload).text

soup = BeautifulSoup(data,'html.parser')

goods=soup.find_all('ul',class_='gridList')[-1]


allgoods=goods.find_all('a','sc-gsWcmt grZHMV')


cursor = db.conn.cursor()
print(allgoods)

# for row in allgoods:
#       link = row.get('href')  
#       photo = row.find('img',class_="sc-bdnxRM sc-gtsrHT gzplcZ ejNgCR").get('srcset')
#       print(photo)
      # photo = photo.split()[0] # 切割，取第一個索引位置, 以空白    
      
      # title = row.find('span',class_='sc-Arkif sc-khIgEk sc-eKYRIR gPtwee hvLVyh tOwMo').text
#       price = row.find('span',class_='sc-Arkif fYIZbn').text
#       price = price.replace('$','').replace(',','')
    
    
#       print(link)
#       print(photo)
#       print(title)
#       print(price)
#       print()
    

#       sql = "select * from goods where name='{}' ".format(title)
    
#       cursor.execute(sql)
#       db.conn.commit()
    
#       if cursor.rowcount == 0 :  # 表示沒有該產品
#           sql = "insert into goods(name,price,goods_url,photo_url,create_date,discount) values('{}','{}','{}','{}','{}','0')".format(title,price,link,photo,todayS)
#           cursor.execute(sql)
#           db.conn.commit()
        
    
db.conn.close()    
    
    
    



