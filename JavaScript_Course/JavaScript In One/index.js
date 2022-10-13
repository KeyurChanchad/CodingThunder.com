// 1. Ways to print in JavaScript
// console.log("Hello World");    //write in console
// alert("me");
// document.write("this is document write")   //write in browser
// console.log({"name":"keyur", "roll no": 10})   //this is object

// 2. Javascript console API
// console.log("Hello World", 4 + 6, "Another log");
// console.warn("this is warning");
// console.error("This is an error");
// console.assert(1> 100, "1 is grater than 100")
// console.clear()
// console.table({Rollno:10, Name:"keyur",Filled:"BCA"})


// 3. JavaScript Variables
// What are Variables? - Containers to store data values

/*
multi 
line 
commment
*/

var number1 = 34;
var number2 = 56;
// console.log(number1 + number2);

// 4. Data types in JavaScript
// Numbers
var num1 = 455;
var num2 = 56.76;

// String
var str1 = "This is a string";
var str2 = 'This is also a string';

// Objects
var marks = {
    ravi: 34,
    shubham: 78,
    harry: 99.977
}
// console.log(marks);

// Booleans
var a = true;
var b = false;
// console.log(a, b);

// var und = undefined;
var und;
// console.log(und);

var n = null;
// console.log(n);
/*
At a very high level, there are two types of data types in JavaScript
1. Primitive data types: undefined, null, number, string, boolean, symbol
2. Reference data types: Arrays and Objects
*/

var arr = [1, 2, "bablu", 4, 5]
// console.log(arr)

// Operators in JavaScript
// Arithmetic Operators
var a = 100;
var b = 10;
// console.log("The value of a + b is ", a+b);
// console.log("The value of a - b is ", a-b);
// console.log("The value of a * b is ", a*b);
// console.log("The value of a / b is ", a/b);

// Assignment Operators
var c = b;
// c += 2;
// c -= 2; // c = c - 2;
// c *= 2;
// c /= 2;
// console.log(c);

// Comparison Operators
var x = 34;
var y = 56;
// console.log(x == y);
// console.log(x >= y);
// console.log(x <= y);
// console.log(x > y);
// console.log(x < y);

// Logical Operators

// Logical and
// 0   0   0 
// 0   1   0
// 1   0   0 
// 1   1   1

// console.log(true && true)
// console.log(true && false)
// console.log(false && true)
// console.log(false && false)

// Logical or
// console.log(true || true)
// console.log(true || false)
// console.log(false || true)
// console.log(false || false)

// Logical not
// console.log(!false);
// console.log(!true);

// Function in JavaScript
function avg(a, b) {
    c = (a + b) / 2;
    return c;
}
// DRY = Do not repeat yourself
c1 = avg(4, 6);
c2 = avg(14, 16);
// console.log(c1, c2);

// Conditionals in JavaScript
/*
var age = 41;
// Single if statement
if(age > 18){
    console.log('You can drink rasna water');
}
// if - else statement
// if(age > 18){
//     console.log('You can drink rasna water');
// }
// else{
//     console.log('You cannot drink rasna water');
// }

age = 25;
// if-else Ladder
if(age > 32){
    console.log("You are not a kid");
}
else if(age >26){
    console.log("Bachhe nahi rahe");
}
else if(age >22){
    console.log("Yes Bachhe nahi rahe");
}
else if(age >18){
    console.log("18 Bachhe nahi rahe");
}
else{
    console.log("Bachhe rahe");
}
console.log("End of ladder");
*/

var arr = [1, 2, 3, 4, 5, 6, 7];
// console.log(arr);
// for(var i=0;i<arr.length;i++){
//     if(i==2){
//         // break;
//         continue;
//     }
//     console.log(arr[i])
// }

// arr.forEach(function(element){
//     console.log(element);
// })
// const ac = 0;
// ac++;
// ac = ac +1;
// let j = 0;
// while(j<arr.length){
//     console.log(arr[j]);
//     j ++;
// }

// do{
//     console.log(arr[j]);
//     j++;
// } while (j < arr.length);

// Array Methods in Javascript
let myArr = ["Fan", "Camera", 34, null, 93.25, undefined, true];
// console.log(myArr.length);
// myArr.pop();
// myArr.push("keyur")
// myArr.shift()
// const newLen = myArr.unshift("Keyur")
// console.log(newLen);
// console.log(myArr);

// String Methods in JavaScript
let myLovelyString = "Keyur is a good boy good good keyur";
// console.log(myLovelyString.length)
// console.log(myLovelyString.indexOf("good"))   //first occurance
// console.log(myLovelyString.lastIndexOf("good"))
// console.log(myLovelyString.substring(5, 20))
// console.log(myLovelyString.split(" "))
// console.log(myLovelyString.endsWith("babalu"))
// console.log(myLovelyString.toUpperCase())
// console.log(myLovelyString.charAt(9))
// console.log(myLovelyString.slice(1,4))
// d = myLovelyString.replace("Keyur", "Chanchad");
// d = d.replace("good", "bad");
// console.log(d, myLovelyString)

let myDate = new Date();
// console.log(myDate.getTime());
// console.log(myDate.getFullYear());
// console.log(myDate.getDay());
// console.log(myDate.getMinutes());
// console.log(myDate.getHours());
// console.log(myDate.getMonth())
// console.log(myDate.toLocaleDateString())
// console.log(myDate.toISOString())
// console.log(myDate.toLocaleString())
 
// DOM Manipulation Document Object Model
let elem = document.getElementById('click');
// console.log(elem);

let elemClass = document.getElementsByClassName("container")
// let elemClass = document.getElementsByClassName("container")[0].classList.add("box-first");
// console.log(elemClass);
// elemClass[0].style.background = "yellow";
elemClass[0].classList.add("bg-primary")
elemClass[0].classList.add("text-success")
elemClass[1].style.textAlign = "center";
// console.log(elem.innerHTML);
// console.log(elem.innerText); 

// console.log(elemClass[0].innerHTML);
// console.log(elemClass[0].innerText); 
tn = document.getElementsByTagName('div')
// console.log(tn)
createdElement = document.createElement('p');
createdElement.innerText = "This is a created para";
tn[0].appendChild(createdElement);
createdElement2 = document.createElement('b');
createdElement2.innerText = "This is a created bold";
tn[0].replaceChild(createdElement2, createdElement);
//tn[0].removeChild(createdElement2); ---> removes an element
 
// Selecting using Query
// sel = document.querySelector('.container')
// console.log(sel)
// sel = document.querySelectorAll('.container')
// console.log(sel)

function clicked(){
    console.log('The button was clicked')
}

// window.onload = function(){
//     console.log('The document was loaded')
// }

// Events in JavaScript
// firstContainer.addEventListener('click', function(){
//     document.querySelectorAll('.container')[0].innerHTML = "<b> We have clicked</b>"
//     console.log("Clicked on Container")
// })

 
// firstContainer.addEventListener('mouseover', function(){
//     console.log("Mouse on Container")
// })

// firstContainer.addEventListener('mouseout', function(){
//     console.log("Mouse out of Container");
// })

// when remove mouse on clicked mouseup evenet fire 
// let prevHTML = document.querySelectorAll('.container')[1].innerHTML;
// firstContainer.addEventListener('mouseup', function(){
//     document.querySelectorAll('.container')[1].innerHTML = prevHTML;
//     console.log("Mouse up when clicked on Container");
// })

// when clicked mouse down event fire 
// firstContainer.addEventListener('mousedown', function(){
//     document.querySelectorAll('.container')[1].innerHTML = "<b> We have clicked</b>"
//     console.log("Mouse down when clicked on Container");
// })


// Arrow Functions
// function summ(a, b){
//     return a+b;
// }
summ = (a,b)=>{
    return a+b;
}

logKaro = ()=>{
    document.querySelectorAll('.container')[1].innerHTML = "<b> Set interval fired</b>"
    console.log("I am your log")
}
// SetTimeout and setinterval
clr = setTimeout(logKaro, 5000);
// clr = setInterval(logKaro, 2000);
// it return id by that you clear it
// use clearInterval(clr)/clearTimeout(clr) to cancel setInterval/setTimeout

// JavaScript localStorage
// localStorage.setItem('name', 'keyur') 
// localStorage 
// localStorage.getItem('name')
// localStorage.removeItem('name')
// localStorage.clear();

// Json 
// obj = {name: "harry", length: 1, a: {this: 'tha"t'}}
// jso = JSON.stringify(obj);
// console.log(typeof jso)
// console.log(jso)
// parsed = JSON.parse(`{"name":"keyur","length":1,"a":{"this":"that"}}`)
// console.log(parsed);

// Template literals - Backticks
a = 34;
// console.log(`this is my ${a}`)
