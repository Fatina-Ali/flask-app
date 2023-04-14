# -*- coding: utf-8 -*- 

import sqlite3

db=sqlite3.connect("app.db")

cur=db.cursor()
# cur.execute(' DROP TABLE accounts ')
cur.execute(""" CREATE TABLE IF NOT EXISTS `DonationRequests`('request_id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'userName' CHAR(200) ,'phone' INTEGER ,'Email' CHAR(200),'address' CHAR(200),
            'order_status' CHAR(40)  ,'orderDate' CHAR(15) ,'amountPaid' INTEGER )""")


cur.execute(""" CREATE TABLE IF NOT EXISTS `services reserved for users`('request_id' INTEGER PRIMARY KEY AUTOINCREMENT,'service_id' INTEGER NOT NULL ,
            'user_id' INTEGER NOT NULL  ,'order_status' CHAR(40) NOT NULL ,'dateOF_serviceRequest' CHAR(15) NOT NULL,'rating' INTEGER NOT NULL)""")

cur.execute("""CREATE TABLE IF NOT EXISTS 'services' ('service_id' INTEGER PRIMARY KEY AUTOINCREMENT, 'service_img' CHAR(200) NOT NULL,
            'title' CHAR(200) NOT NULL, 'number_of_beneficiaries' INTEGER NOT NULL , 
            'service_type_id' INTEGER NOT NULL ,'price' INTEGER NOT NULL ,'deleted' INTEGER NOT NULL )""")

cur.execute("""CREATE TABLE IF NOT EXISTS 'users' ('user_id' INTEGER PRIMARY KEY AUTOINCREMENT , 'name' CHAR(200) NOT NULL,
            'email' CHAR(200) NULL,'phone' INTEGER NOT NULL, 'address_of_residence' CHAR(200) NOT NULL)""")


cur.execute("""CREATE TABLE IF NOT EXISTS 'accounts' ( 'account_id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
            'user_name' CHAR(200),'Email' CHAR(200),'password' CHAR(100),'userRole' CHAR(50) )""")

cur.execute("""CREATE TABLE IF NOT EXISTS 'types Of services' ( 'type_id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
            'type_name' CHAR(200), 'image_path' CHAR(200), 'deleted' INTEGER NOT NULL )""")



cur.execute("""CREATE TABLE IF NOT EXISTS 'budget' ( 'request_id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,'typeOfRequest' CHAR(200),'materialValue' INTEGER)""")
cur.execute(""" INSERT INTO 'accounts' (user_name,Email,password,userRole) VALUES(?,?,?,?)""" ,('fatina ali','fatina@gmail.com','fatina333','admin'))




db.commit()





