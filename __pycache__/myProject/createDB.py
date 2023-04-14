# -*- coding: utf-8 -*- 

import sqlite3

db=sqlite3.connect("app.db")

cur=db.cursor()
# cur.execute("""DROP TABLE admins_info""")
cur.execute(""" CREATE TABLE IF NOT EXISTS `services reserved for users`('service_id' INTEGER NOT NULL ,
            'user_id' INTEGER NOT NULL)""")

cur.execute("""CREATE TABLE IF NOT EXISTS 'services' ('service_id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'title' CHAR(200) NOT NULL, 'number_of_beneficiaries' INTEGER NOT NULL )""")

cur.execute("""CREATE TABLE IF NOT EXISTS 'users' ('user_id' INTEGER PRIMARY KEY AUTOINCREMENT , 'name' CHAR(200), 'email' CHAR(200) NULL,
            'phone' INTEGER NULL, 'address_of_residence' CHAR(200) )""")


cur.execute("""CREATE TABLE IF NOT EXISTS 'admins_info' ('admin_name' CHAR(200) ,  'admin_id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT)""")

cur.execute(""" INSERT INTO 'admins_info' (admin_name) VALUES(?)""" ,('Mostafa Alaysh',))

cur.execute(""" INSERT INTO services (title , number_of_beneficiaries) VALUES(?,?) """ ,('frizer',5))

cur.execute(""" INSERT INTO services (title , number_of_beneficiaries) VALUES(?,?) """ ,('window',6))

db.commit()

