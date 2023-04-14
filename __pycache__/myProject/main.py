
from flask import Flask , render_template , jsonify , request , redirect , url_for
import functions

app = Flask(__name__)


@app.route("/getDATA")
def data():
    da=functions.get_services()
    return da

@app.route("/")
def home():
    return render_template("home.html")


    


# @app.route("/gg/<data>" , methods=["POST"])
# def h(data):
#     print(data)
#     return data


@app.route("/addUSER/<service_id>" , methods=["POST"])
def add_user(service_id):
    name=request.form.get("name")
    email=request.form.get("email")
    phone=request.form.get("phone")
    address=request.form.get("address")
    functions.add_USER(name , email , phone , address)
    functions.delete_aNumber_of_beneficiaries(service_id)
    user_id=functions.get_userID_by_name(name)
    functions.store_inThe_reservedSERVICES_table(service_id,user_id)
    return redirect(url_for("home"))

@app.route("/service/<ser_id>") 
def form(ser_id):  
    return render_template("get.html" , service_id=ser_id)

# @app.route("/click/") 
# def click():
#     services=get_services()
#     return render_template("admin.html" ,services=services)

@app.route("/update")
def updateService():
    return "<h1>test</h1>"



@app.route("/delete/<service_id>")
def deleteService(service_id):
    functions.delete_service_by_id(service_id)
    return redirect(url_for("adminPAGE"))

@app.route("/adminPAGE")
def adminPAGE():
    return render_template("admin.html")





if __name__== '__main__':     

    app.run(debug=True , port=3000)  