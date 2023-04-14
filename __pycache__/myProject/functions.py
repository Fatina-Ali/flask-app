
import sqlite3
import os
from flask import jsonify

BASE_DIR = os.path.dirname(os.path.realpath(__file__)) 
DB_PATH = os.path.join(BASE_DIR, 'app.db') 

def get_services(): 
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    query=cursor.execute('''SELECT * FROM services''')
    li=[]
    services = query.fetchall()
    for i in services:
        dec={}
        dec["services_id"] = i[0]
        dec["title"] = i[1]
        dec["number_of_beneficiaries"] = i[2]
        li.append(dec)
    response = jsonify(li) 
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

def get_service_by_id(service_id): 
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    service_id = int(service_id) 
    query = cursor.execute('''SELECT title, number_of_beneficiaries FROM services WHERE service_id=?''',(service_id,)) 
    service = query.fetchone() 
    return service

def delete_service_by_id(service_id): 
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    cursor.execute('''DELETE FROM services WHERE service_id=?''',(service_id,)) 
    db.commit()

def create_service(title, number_of_beneficiaries): 
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    cursor.execute('''INSERT INTO services(title, number_of_beneficiaries) VALUES(?,?)''', (title, number_of_beneficiaries)) 
    db.commit()

def add_USER(name , email , phone , address):
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor()  
    cursor.execute('''INSERT INTO users(name, email,phone,address_of_residence) VALUES(?,?,?,?)''', (name, email,phone,address))   
    db.commit()


def delete_aNumber_of_beneficiaries(service_id):
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor()
    query=cursor.execute(''' SELECT number_of_beneficiaries FROM services WHERE service_id=? ''' ,(service_id,))
    oldValue=query.fetchone()[0]
    cursor.execute(f''' UPDATE services SET number_of_beneficiaries= "{oldValue-1}" WHERE service_id=?''',(service_id,))    
    db.commit()


def store_inThe_reservedSERVICES_table(service_id ,user_id):
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor()    
    cursor.execute("INSERT INTO `services reserved for users`(service_id ,user_id) VALUES(?,?)", (service_id ,user_id))
    db.commit() 

def get_userID_by_name(name): 
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor()  
    query = cursor.execute('''SELECT user_id FROM users WHERE name=?''',(name,)) 
    user_id = query.fetchone()[0]
    return user_id
