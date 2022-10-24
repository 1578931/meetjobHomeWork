# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 19:35:55 2022

@author: 大班
"""

import pymysql

dbsetting = {
    "host":"127.0.0.1",
    "port":3306,
    "user":"root",
    "password":"123456789",
    "db":"Jobs",
    "charset":"utf8"
    }

conn = pymysql.connect(**dbsetting)