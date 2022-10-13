console.log("This is tutorial 28");

// Object literal : Object.prototype
let myobj = {
    name: "Keyur",
    channel: "Code With Keyur",
    address: "Mars"
}

//prototype means it already writen function/code we simply use. If we make prototype than it available for all. 
//declare prototype
function Obj(givenName){
    this.name = givenName
}

Obj.prototype.getName = function (){
    return this.name;
}

Obj.prototype.setName = function (newName){
  this.name = newName;
}

let obj2 = new Obj("Keyur");
console.log(obj2);
 