console.log("This is tutorial 56 on for-in and for-of loops");

let people = ["Keyur", "Kishan", "Sager", "Rakesh", "Prashant"];


// **********For in loop***********
// Traditional for loop:
// for (let index = 0; index < people.length; index++) {
//     const element = people[index];
//     console.log(element);   
// }


// 1. ITERATING AN OBJECT
let obj = {
    name: "Keyur",
    language: "JavaScript",
    hobbies: "Android app development"
}
// console.log(obj);
// 1.1 Iterating an object using Traditional for loop:
// for (let index = 0; index < Object.keys(obj).length; index++) {
//     const element = obj[Object.keys(obj)[index]];
//     console.log(element);   
// }

// 1.2 Iterating an object using for-in loop:
// for (let key in obj){
//     console.log(obj[key]);
// }

// 2. ITERATING A STRING
// We can use for in with strings to loop through all the characters

myString = "This is my string";
// for (let char in myString){
//     console.log(myString[char]);
// }

// for (let index = 0; index < myString.length; index++) {
//     const element = myString[index];
//     console.log(element)
// }
// Quiz: Use traditional for loop to iterate through the same string


// **********For of loop***********
console.log("*****************For of loop starts here**************")

for(let name of people){
    console.log(name);
}

// for (let name in people){
//     console.log(people[name]); 
// }

for(let name of myString){
    console.log(name);
}
