// function httpGetAsync(theUrl, callback) {
//     var xmlHttp = new XMLHttpRequest();
//     xmlHttp.onreadystatechange = function () {
//     if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
//         callback(xmlHttp.responseText);
//     }
//     xmlHttp.open("GET", theUrl, true); 
//     xmlHttp.send();
// }

// window.addEventListener("load", function () {
//     httpGetAsync("http://127.0.0.1:3000/getDATA", function (r) {
//         data= JSON.parse(r)
            
//         for (column=0; column< data.length ; column++){
//             createDIV=document.createElement("div");
//             createDIV.className="div" + data[column]["services_id"];
//             createDIV.style = "width:200px"
//             createH4= document.createElement("h4");
//             createH4.appendChild(document.createTextNode(data[column]["services_id"] + ":رقم الخدمة"))
//             createH3 = document.createElement("h3");
//             createH3.appendChild(document.createTextNode(data[column]["title"]))
//             createP = document.createElement("p");
//             createP.appendChild(document.createTextNode(data[column]["number_of_beneficiaries"] + ":عدد المستفيدين"))   
//             createa = document.createElement("a");
//             createa.className="a"
//             createa.setAttribute("href", "service/" + `${data[column]["services_id"]}`)
//             createa.id=`${ data[column]["services_id"] }`
//             createa.appendChild(document.createTextNode("حجز الخدمة"))  
//             createDIV.appendChild(createH4); createDIV.appendChild(createH3); createDIV.appendChild(createP); createDIV.appendChild(createa); 
//             document.getElementById("div1").append(createDIV)                     
//         }
//     })
// })

console.log("hello")
