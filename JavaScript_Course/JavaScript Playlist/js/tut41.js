/*
function mul(a, b) {
    return a * b
    }//calling function
mul(3,3) //returns 9

let addition = function(x,y) {
 return x + y;
}
console.log(addition(10,10)); // returns 20

let addition = (x,y) => x + y;
console.log(addition(10,10)); // 20;

let greet = () => {
   return "Hello World!";
 } 

 greet = () => "Hello World!";
*/


console.log('this is tutorial 41');

// ARROW FUNCTIONS

// Creating a regular function
// const keyur = function (){
//     console.log("This is the best person ever")
// }

// Converting it to an arrow function
// const keyur = ()=>{
//     console.log("This is the best person ever")
// }
// keyur();

// function returning something
// const greet = function(){
//     return "Good Morning";
// }

// One liners do not require braces/return
// one line will automatically return
// const greet = () =>  "Good Morning";

// const greet = () =>  ({name: "keyur"});

// Single parameters do not need parenthesis 
// but you will have to put parenthesis if there are multiple paramteres
const greet = name =>  "Good Morning " + name ;



console.log(greet('Keyur'))
