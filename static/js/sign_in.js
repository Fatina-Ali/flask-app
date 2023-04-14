function postRequest(theUrl, objDATA, callback) {
    var xm = new XMLHttpRequest();
    xm.onreadystatechange = function () {
        if (xm.readyState == 4 && xm.status == 200) {
            callback(this.responseText)
        }
    }
    xm.open("POST", theUrl);
    xm.send(JSON.stringify(objDATA))
}
const sign_in_btn=document.querySelector("#sign-in-btn");
const sign_up_btn=document.querySelector("#sign-up-btn");
const container=document.querySelector(".container");

sign_up_btn.addEventListener('click', () =>{
    container.classList.add("sign-up-mode")

});
sign_in_btn.addEventListener('click', () =>{
    container.classList.remove("sign-up-mode")

})

document.getElementById("btn_signUP").onclick=() =>{
    Username=document.getElementById("Username").value;
    Email=document.getElementById("Email").value;
    Password=document.getElementById("Password").value;
    Confirm_Password=document.getElementById("Password2").value;

    if(Username!="" && Email!="" && Password!="" && Confirm_Password!=""){
        if(Email.length<10 | Email.indexOf('@')==-1){
            window.alert('invalid Email');
            document.getElementById("Email").value=''
        }
       
        if(Password==Confirm_Password){
            if(Password.length<8){
                window.alert('invalid Password');
                document.getElementById("Password").value=''
                document.getElementById("Password2").value=''
            }
        }
        if(Password!=Confirm_Password){
            window.alert('Wrong Password');
            document.getElementById("Password2").value=''
        }

        if(Password==Confirm_Password & Password.length>=8 & Email.length>=10 & Email.indexOf('@')!=-1){
            obj={
                "Username":Username,
                "Email":Email,
                "Password":Password
            }

            postRequest("http://127.0.0.1:3000/sign-up",obj,function(r){
                if(r=="invalid name"){
                    window.alert("invalid name");
                    document.getElementById("Username").value=''
                }
                if(r=="the name is accepted"){
                    window.open(`http://127.0.0.1:3000/openUserPage${Username}`)
                }
            })
        }

    

    }
    else{
        window.alert("Please fill in all the fields !")
    }


}
document.getElementById("btn_signIN").onclick=function(){
    Username=document.getElementById("UsernamE").value;
    Password=document.getElementById("PassworD").value;
    if(Username!="" && Password!=""){
        obj={
            "user_name":Username,
            "password":Password
        } 
    
        postRequest("http://127.0.0.1:3000/sign-in",obj,function(data){
            if(data== "wrong password" || data == "the name is not found"){
                window.alert(data)
                Username='';
                Password='';
                window.open("http://127.0.0.1:3000/LogIN")
                
            }
            if(data=="admin"){
                window.open("http://127.0.0.1:3000/adminPAGE")
            }
    
            if(data=="user"){
                window.open(`http://127.0.0.1:3000/openUserPage${Username}`)
            }
            
        })
    }
    else{
        window.alert("Please fill in all the fields !")
    }

}