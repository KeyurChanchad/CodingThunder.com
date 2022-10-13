console.log("This is tutorial 59")

// Symbols
const sym1 =  Symbol('My identifier');
const sym2 =  Symbol('My identifier');
// console.log('Symbol is ', sym1);
// console.log('Type of Symbol is ', typeof sym1);
console.log(sym1 === sym2);

const a = "this is";
const b = "this is";

// console.log(a === b);
// console.log(null === null);
// console.log(undefined === undefined);

const k1 = Symbol('identifier for k1');
const k2 = Symbol('identifier for k2');

myObj = {};
myObj[k1] = "Keyur";
myObj[k2] = "Chanchad";
myObj["name"] = "Good boy"
myObj[4] = "Good int"


// console.log(myObj);
// console.log(myObj[k1]);
// console.log(myObj[k2]);
// console.log(myObj.k2); // !! ALERT !!: cannot do this to get Chanchad because symbole it is same as myObj["k2"] 

// obj = {
//     name : 'I am good boy.'
// }
// console.log(obj.name);

// Symbols are ignored in for in loop
// for(key in myObj){
//     console.log(key, myObj[key])
// }

// console.log(JSON.stringify(myObj));
