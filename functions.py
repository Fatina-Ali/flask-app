
from argparse import Namespace
import sqlite3
import os
from flask import jsonify


BASE_DIR = os.path.dirname(os.path.realpath(__file__)) 
DB_PATH = os.path.join(BASE_DIR, 'app.db') 


############## start functions get data ###############
def get_types(): 
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    query=cursor.execute('''SELECT * FROM  'types Of services' WHERE deleted=? ''',(0 ,))
    li=[]
    services = query.fetchall()
    for i in services:
        dec={}
        dec["type_id"] = i[0]
        dec["type_name"] = i[1]
        dec["image_path"] = i[2]
        li.append(dec)
    response = jsonify(li) 
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

def getUserRequests(obj):
    userName=obj['userName']
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    query=cursor.execute('''SELECT * FROM `users` ''' )
    rows=query.fetchall()

    for row in rows:
        global userId
        if(userName.lower()==row[1].lower()):
            userId=row[0]
        else:
            userId='not defined'
    if userId !='not defined':
        quer1=cursor.execute('''SELECT * FROM `services reserved for users` WHERE user_id=? ''' ,(userId,))
        orders=quer1.fetchall()
        ordersOfUser=[]
        for order in orders:
            userOrder={}
            querySER=cursor.execute('''SELECT title FROM `services` WHERE service_id=? ''' ,(order[1],))
            serviceName=querySER.fetchall()[0][0]
            userOrder['requestId']=order[0]
            userOrder['requestService']=serviceName
            userOrder['orderDate']=order[4]
            userOrder['orderStatus']=order[3]
            userOrder['rating']=order[5]
            ordersOfUser.append(userOrder)
        response = jsonify(ordersOfUser) 
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    else:
        return ''

def getDonationOrders():
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    query=cursor.execute('''SELECT * FROM DonationRequests ''')
    li=[]
    orders = query.fetchall()
    for i in orders:
        dec={}
        dec["request_id"] = i[0]
        dec["userName"] =i[1]
        dec["phone"] = i[2]
        dec["Email"] = i[3]
        dec["address"] = i[4]
        dec["order_status"] = i[5]
        dec["orderDate"] = i[6]
        dec["amountPaid"] = i[7]
        li.append(dec)
    response = jsonify(li) 
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

def getServicesByTypeID(type_id): 
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    query=cursor.execute('''SELECT * FROM services WHERE service_type_id=? AND deleted=? ''',(type_id,0 ,))
    li=[]
    services = query.fetchall()
    for i in services:
        dec={}
        dec["service_id"] = i[0]
        dec["service_img"]=i[1]
        dec["title"] = i[2]
        dec["number_of_beneficiaries"] = i[3]
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


def get_userID_by_name(name,phone): 
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor()  
    query = cursor.execute('''SELECT user_id FROM users WHERE name=? AND phone=?''',(name,phone,)) 
    user_id = query.fetchone()
    return(user_id[0])


def get_accountId_byName(name): 
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    query1 = cursor.execute('''SELECT * FROM accounts ''') 
    allData=query1.fetchall()
    for row in allData:
        if (name.lower())==((row[1]).lower()):
            accountId=row[0]
            break
    return(int(accountId))

def getBudget():
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor()
    query=cursor.execute(f''' SELECT * FROM budget''' )
    allOrders=query.fetchall()
    query1=cursor.execute(f''' SELECT SUM (materialValue) FROM budget''' )
    Budget=query1.fetchone()[0]
    li=[]
    for order in allOrders:
        dec={}
        dec['request_id'] = order[0]
        dec['typeOfRequest'] = order[1]
        dec["materialValue"] = order[2]
        li.append(dec)
    Budget={'Budget':Budget}
    li.append(Budget)
    response = jsonify(li) 
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

def bringAll_theServices(): 
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    query=cursor.execute('''SELECT * FROM services WHERE deleted=?''',(0 ,))
    li=[]
    services = query.fetchall()
    for i in services:
        dec={}
        dec["service_id"] = i[0]
        dec["service_img"] =i[1]
        dec["title"] = i[2]
        dec["number_of_beneficiaries"] = i[3]
        dec["price"]=i[5]
        li.append(dec)
    response = jsonify(li) 
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response



def viewOrders():
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    query=cursor.execute('''SELECT * FROM `services reserved for users` ''')
    rows = query.fetchall()
    listOfOrders=[]
    for row in rows:
        orderInformation={}
        querySER=cursor.execute('''SELECT * FROM `services` WHERE service_id=? ''' ,(row[1],))
        serviceInformation=querySER.fetchall()
        queryUSER=cursor.execute('''SELECT * FROM `users` WHERE user_id=? ''' ,(row[2],))
        UserInformation=queryUSER.fetchall()

        orderInformation["requestId"]=row[0]
        orderInformation["requestService"]=serviceInformation[0][2]
        orderInformation["userName"]=UserInformation[0][1]
        orderInformation["userPhone"]=UserInformation[0][3]
        orderInformation["orderDate"]=row[4]
        orderInformation["orderStatus"]=row[3]
        orderInformation["order Evaluation"]=row[5]
        listOfOrders.append(orderInformation)
    response = jsonify(listOfOrders) 
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


############## end functions get data ###############


############## start functions update data ###############


def updateStatusTocanceL(obj):
    request_id=obj["requestId"]
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    cursor.execute(f''' UPDATE "services reserved for users" SET order_status= "cancelled" 
    WHERE request_id=?''',(request_id,))
    db.commit()

def updateStatus_donationOrders(obj):
    request_id=obj["requestId"]
    status=obj['newStatus']
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    cursor.execute(f''' UPDATE "DonationRequests" SET order_status= "{status}" 
    WHERE request_id=?''',(request_id,))
    query=cursor.execute(f''' SELECT amountPaid FROM "DonationRequests" 
    WHERE request_id=?''',(request_id,))
    amountPaid=query.fetchall()[0][0]
    d=int(amountPaid)
    cursor.execute("INSERT INTO `budget` (typeOfRequest,materialValue) VALUES(?,?)", ('donation' ,+d))
    db.commit()


def updateStatusToSucceffullY(obj):
    request_id=obj["requestId"]
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    cursor.execute(f''' UPDATE "services reserved for users" SET order_status= "successfully" 
    WHERE request_id=?''',(request_id,))
    query=cursor.execute(f''' SELECT service_id FROM "services reserved for users" 
    WHERE request_id=?''',(request_id,))
    serviceId=query.fetchall()[0][0]
    query1=cursor.execute(f''' SELECT price FROM "services" 
    WHERE service_id=?''',(serviceId,))
    price=query1.fetchall()[0][0]
    d=int(price)
    cursor.execute("INSERT INTO `budget` (typeOfRequest,materialValue) VALUES(?,?)", ('service' ,-d))
    db.commit()

   

def updateRatingInTheDataBase(obj):
    request_id=obj["requestId"]
    starsNumber=obj["starsNumber"]
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    cursor.execute(f''' UPDATE "services reserved for users" SET rating= "{starsNumber}" 
    WHERE request_id=?''',(request_id,))
    db.commit()


def UpdateServiceData(obj):
    newName=obj["newName"]
    serID=obj["serID"]
    newNUMBER=obj["newNumber"]
    service_img=obj["service_img"]
    price=obj["price"]
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    cursor.execute(f''' UPDATE services SET title= "{newName}" WHERE service_id=?''',(serID,))
    cursor.execute(f''' UPDATE services SET number_of_beneficiaries= "{newNUMBER}" WHERE service_id=?''',(serID,)) 
    cursor.execute(f''' UPDATE services SET service_img= "{service_img}" WHERE service_id=?''',(serID,)) 
    cursor.execute(f''' UPDATE services SET price= "{price}" WHERE service_id=?''',(serID,)) 
    db.commit()


def UpdateTypeData(obj):
    newName=obj["newName"]
    typeID=obj["typeId"]
    imagePath=obj["imagePath"]
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    cursor.execute(f''' UPDATE "types Of services" SET type_name= "{newName}" WHERE type_id=?''',(typeID,))
    cursor.execute(f''' UPDATE "types Of services" SET image_path= "{imagePath}" WHERE type_id=?''',(typeID,))
    db.commit()



############## end functions update data ###############

############## start functions delete data ###############

def delete_service_by_id(obj):
    serID=obj["serID"] 
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    cursor.execute(f''' UPDATE services SET deleted= "{1}" WHERE service_id=?''',(serID,))
    db.commit()

def deleteDonationOrder(id):
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    cursor.execute(f''' DELETE FROM DonationRequests WHERE request_id=?''',(id,))
    db.commit()


def deleteOrder(id):
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    cursor.execute(f''' DELETE FROM `services reserved for users` WHERE request_id=?''',(id,))
    db.commit()


def delete_type_by_id(obj):
    typeId= obj["typeID"]  
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    cursor.execute(f''' UPDATE "types Of services" SET deleted= "{1}" WHERE type_id=?''',(typeId,))
    cursor.execute(f''' UPDATE  services SET deleted= "{1}" WHERE service_type_id=?''',(typeId,))
    db.commit()

def delete_aNumber_of_beneficiaries(service_id):
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor()
    query=cursor.execute(''' SELECT number_of_beneficiaries FROM services WHERE service_id=? ''' ,(service_id,))
    oldValue=query.fetchone()[0]
    if oldValue==0:
        cursor.execute(f''' UPDATE services SET deleted={1} WHERE service_id=?''',(service_id,)) 
    elif oldValue > 0:
        cursor.execute(f''' UPDATE services SET number_of_beneficiaries= "{oldValue-1}" WHERE service_id=?''',(service_id,))    
    db.commit()


############## start functions delete data ###############


############## start functions add data ###############
def create_service(title, number_of_beneficiaries): 
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    cursor.execute('''INSERT INTO services(title, number_of_beneficiaries) VALUES(?,?)''', (title, number_of_beneficiaries)) 
    db.commit()

def add_USER(name , email, phone , address):
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor()  
    query=cursor.execute(''' SELECT * FROM users ''' )
    data=query.fetchall()
    phoneNumbers=[]
    usersNames=[]
    for Tuple in data:
        phoneNumbers.append(Tuple[3]) 
        usersNames.append(Tuple[1].lower())

    nameLower=name.lower()

    if(nameLower in usersNames):
        if(phone in phoneNumbers):
            return 'good'
        return 'invalid name'
    else:
        cursor.execute('''INSERT INTO users(name, email,phone,address_of_residence) VALUES(?,?,?,?)''', (nameLower, email,phone,address)) 
        db.commit()
        return 'good'
     
def add_donationRequest(name,email,phone,address,donation,requestDate):
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    d=int(donation)
    cursor.execute('''INSERT INTO DonationRequests(userName,phone,Email,address,order_status,orderDate,amountPaid)VALUES(?,?,?,?,?,?,?)''', (name,phone,email,address,'pending',requestDate,+d,))
    db.commit()
    return 'good'
  

def store_inThe_reservedSERVICES_table(service_id ,user_id,requestDate):
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor()    
    cursor.execute('''INSERT INTO `services reserved for users` (service_id ,user_id , dateOF_serviceRequest,order_status,rating) VALUES(?,?,?,?,?)''', (service_id ,user_id,requestDate,"Pending",0))
    db.commit() 

def sign_in(DIC):
    userName=(DIC["user_name"]).lower()
    password=(DIC["password"])
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor()  
    query = cursor.execute('''SELECT user_name FROM accounts ''')
    rows=query.fetchall()
    namesInList=[] 
    for row in rows:
        namesInList.append(row[0].lower())

    if (userName in namesInList) :
        accountId=get_accountId_byName(userName)
        query1=cursor.execute('''SELECT password,userRole FROM accounts WHERE account_id=?''',(accountId,))
        userInformation = query1.fetchall()
        if password==userInformation[0][0]:
            return userInformation[0][1]
        else:
            return "wrong password"
    else:
        return "the name is not found"


def addServicE(OBJ):
    nameNewService=OBJ["nameService"]
    number_of_Beneficiaries=OBJ["number_ofBeneficiaries"]
    serviceTypeID = OBJ["serviceTypeID"]
    imgPath=OBJ["service_img"]
    price=OBJ["price"]
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    cursor.execute('''INSERT INTO `services` (service_img, title , number_of_beneficiaries,service_type_id ,deleted,price)
    VALUES(?,?,?,?,?,?)''', (imgPath, nameNewService , number_of_Beneficiaries, serviceTypeID , 0,price))
    db.commit()


def addType(obj):
    nameNewType=obj["nameType"]
    imagePath=obj["imagePath"]
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    cursor.execute("INSERT INTO `types Of services` (type_name , image_path ,deleted) VALUES(?,?,?)", (nameNewType , imagePath , 0))
    db.commit()



def checking_that_the_name_isNOT_repeated(new_name):
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor()
    query=cursor.execute('''SELECT user_name FROM accounts ''')
    rows=query.fetchall()
    names=[]
    for row in rows:
        names.append((row[0]).lower())
    if (new_name.lower()) in names:
        return "invalid name"
    else:
        return "the name is accepted"


def addAccount(obj):
    Username=obj["Username"]
    Email=obj["Email"]
    Password=obj["Password"]
    db = sqlite3.connect(DB_PATH) 
    cursor = db.cursor() 
    cursor.execute("INSERT INTO `accounts` (user_name , Email ,password,userRole) VALUES(?,?,?,?)", (Username , Email , Password,"user"))
    db.commit()


   
