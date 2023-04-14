import ast
import os
from werkzeug.utils import secure_filename
from flask import Flask , render_template ,request , redirect , url_for,flash,Markup
import functions
import json
from datetime import date

# from flask_mail import Mail, Message

UPLOAD_FOLDER='./static/images'

ALLOWED_EXTENSIONS=set(['txt' , 'png' , 'jpg' ,'jpeg' , 'gif','svg'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER



#################  start render template  ##################

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/servicesPage/<typeId>" , methods=['POST' , "GET"])
def servicesPage(typeId): 
    return render_template("servicesByType.html",typeId= typeId)


@app.route('/materialExpenses')
def materialExpenses():
    return render_template('materialExpenses.html')


@app.route('/DonationPage')
def DonationPage():
    return render_template('Donation.html')


@app.route('/DonationOrdersPage')
def DonationOrdersPage():
    return render_template('DonationOrders.html')



@app.route("/openUserPage<Username>")
def openUserPage(Username):
    return render_template("userOwnPage.html",Username=Username)


@app.route("/serviceRequest/<ser_id>/<serviceName>") 
def form(ser_id,serviceName):  
    return render_template("userForm.html" , service_id=ser_id , serviceName=serviceName)


@app.route("/LogIN")
def LogIN():
    return render_template("sign_in.html")


@app.route("/adminPAGE")
def adminPAGE():
    return render_template("adminPAGE.html")


@app.route("/serviceAddPage")
def addSER():
    return render_template("addSERVICE.html")


@app.route("/showALLservices")
def showALLservices():
    return render_template("showAllServices.html")

@app.route("/addType")
def addType():
    return render_template("addType.html")


@app.route("/viewOrders")
def viewOrders():
    return render_template("Orders.html")



################## end render template ##################

########### Start get Data ##################

@app.route("/getTypes")
def types():
    data=functions.get_types()
    return data

@app.route("/getDATA")
def data():
    da=functions.bringAll_theServices()
    return da  

@app.route('/getDonationOrders')
def DonationOrders():
    data=functions.getDonationOrders()
    return data

@app.route("/getOrders")
def getOrders():
    orders=functions.viewOrders()
    return orders

@app.route("/getUserRequest" , methods=['POST'])
def getUserRequest():
    theData=request.get_data()
    dataInObj=json.loads(theData.decode('utf-8'))
    orders=functions.getUserRequests(dataInObj)
    return orders



@app.route('/getBudget')
def getBudget():
    data= functions.getBudget()
    return data

########### End get Data ##################

########### Start update  Data ##################



@app.route("/updateServiceData/<serviceID>", methods=["POST"])
def updateServiceData(serviceID):
    serviceName= request.form.get("serviceName")
    newNumber=request.form.get("number_of_beneficiaries")
    price=request.form.get("price")
    file=request.files['file']
    path=os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)
    imageName=path[16:]
    imagePath=f"images/{imageName}"
    objectContentDATA={
        "serID":int(serviceID),
        "newName":serviceName,
        "newNumber":newNumber,
        "service_img":imagePath,
        "price":price
    }
    functions.UpdateServiceData(objectContentDATA)
    return redirect(url_for("adminPAGE"))

@app.route("/updateTypeData/<typeID>" , methods=["POST"])
def updateTypeData(typeID):
    typeName= request.form.get("typeName")
    file=request.files['file']
    path=os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)
    imageName=path[16:]
    imagePath=f"images/{imageName}"
    objectContentDATA={
        "typeId":int(typeID),
        "newName":typeName,
        "imagePath":imagePath
    }
    functions.UpdateTypeData(objectContentDATA)
    return redirect(url_for('adminPAGE'))

@app.route('/updateStatusTocancel', methods=["POST"])
def updateStatusTocancel():
    theData=request.get_data()
    dataInObj=json.loads(theData.decode('utf-8'))
    functions.updateStatusTocanceL(dataInObj)
    return 'successfully'

@app.route('/updateStatusdonationOrders', methods=["POST"])
def updateStatus_donationOrders():
    theData=request.get_data()
    dataInObj=json.loads(theData.decode('utf-8'))
    print(dataInObj)
    functions.updateStatus_donationOrders(dataInObj)
    return 'successfully'



@app.route('/updateStatusToSucceffully', methods=["POST"])
def updateStatusToSucceffully():
    theData=request.get_data()
    dataInObj=json.loads(theData.decode('utf-8'))
    functions.updateStatusToSucceffullY(dataInObj)
    return 'successfully'


@app.route('/updateRating', methods=["POST"])
def updateRating():
    theData=request.get_data()
    dataInObj=json.loads(theData.decode('utf-8'))
    functions.updateRatingInTheDataBase(dataInObj)
    return 'good'


########### End update  Data ##################


########### Start delete  Data ##################


@app.route("/deleteSER" , methods=["POST"])
def deleteService():
    theData=request.get_data()
    dataInObj=json.loads(theData.decode('utf-8'))
    functions.delete_service_by_id(dataInObj)
    return "successfully"

@app.route("/showservices" , methods=['POST'])
def showservices(): 
    theData=request.get_data()
    dataInObj=json.loads(theData.decode('utf-8'))
    requirdServices=functions.getServicesByTypeID(dataInObj["typeId"])
    return requirdServices

@app.route('/deleteDonationOrder' , methods=['POST'])
def deleteDonationOrder():
    theData=request.get_data()
    dataInObj=json.loads(theData.decode('utf-8'))
    functions.deleteDonationOrder(dataInObj['id'])
    return 'good'


@app.route('/deleteOrder' , methods=['POST'])
def deleteOrder():
    theData=request.get_data()
    dataInObj=json.loads(theData.decode('utf-8'))
    functions.deleteOrder(dataInObj['id'])
    return 'good'


@app.route("/deleteType", methods=["POST"])
def deleteType():
    theData=request.get_data()
    dataInObj=json.loads(theData.decode('utf-8'))
    functions.delete_type_by_id(dataInObj)
    return "successfully"

########### End delete  Data ##################

########### Start add  Data ##################

@app.route("/addUSER/<service_id>" , methods=["POST"])
def add_user(service_id):
    theData=request.get_data()
    dataInObj=json.loads(theData.decode('utf-8'))
    name=dataInObj['name']
    email=dataInObj['email']
    phone=dataInObj['phone']
    address=dataInObj['address']
    requestDate=date.today()
    result=functions.add_USER(name , email , phone , address)
    
    if(result=='invalid name'):
        return result

    else:
        functions.delete_aNumber_of_beneficiaries(service_id)
        user_id=functions.get_userID_by_name(name , phone)
        functions.store_inThe_reservedSERVICES_table(service_id , user_id , requestDate)
        return 'good'


########### End add  Data ##################

########### start input Data of the services and types ##################

@app.route("/input.Data.OF.theType" , methods=["POST"])
def inputData_OF_theType():
    typeName=request.form.get("typeName")
    file=request.files['file']
    path=os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)
    imageName=path[16:]
    imagePath=f"images/{imageName}"
    obj={
        "nameType" : typeName,
        "imagePath" : imagePath
        }
    functions.addType(obj)
    return redirect(url_for('adminPAGE'))

@app.route("/input.Data.OF.theService" , methods=["POST"])
def inputData_OF_theService():
    serviceName=request.form.get("serviceName")
    number_of_beneficiaries=int(request.form.get("number_of_beneficiaries"))
    select=request.form.get("select")
    price=request.form.get("price")
    typeId=int(select[6:])
    file=request.files['file']
    path=os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)
    imageName=path[16:]
    imagePath=f"images/{imageName}"
    obj = {
        "nameService": serviceName ,
        "number_ofBeneficiaries": number_of_beneficiaries ,
        "serviceTypeID" : typeId,
        "service_img":imagePath,
        "price":price
    }
    functions.addServicE(obj)
    return redirect(url_for('adminPAGE'))

########### end input Data of the services and types ##################

############### start shoe services #############
def showservices(): 
    theData=request.get_data()
    dataInObj=json.loads(theData.decode('utf-8'))
    requirdServices=functions.getServicesByTypeID(dataInObj["typeId"])
    return requirdServices
############### end shoe services #############



########### start sign in and sign up #################

@app.route("/sign-in" , methods=["POST"])
def sign_in():
    theData=request.get_data()
    dataInObj=json.loads(theData.decode('utf-8'))
    result=functions.sign_in(dataInObj)
    return result


@app.route("/sign-up" , methods=["POST"])
def sign_up():
    theData=request.get_data()
    dataInObj=json.loads(theData.decode('utf-8'))
    result=functions.checking_that_the_name_isNOT_repeated(dataInObj["Username"])
    if result=="the name is accepted":
        functions.addAccount(dataInObj)
    
    return result

########### end sign in and sign up #################




############# start storage of donor data ###################

@app.route('/Storage-of-DonorData', methods=["POST"])
def Storage_of_DonorData():
    userName=request.form.get('name')
    email=request.form.get('email')
    phone=request.form.get('phone')
    address=request.form.get('address')
    donation=request.form.get('donation')
    requestDate=date.today()
    print(type(requestDate))
    functions.add_donationRequest( userName,email,phone,address,donation,requestDate)
    return redirect(url_for("home"))

############# start storage of donor data ###################


if __name__== '__main__':     

    app.run(debug=True , port=3000)  