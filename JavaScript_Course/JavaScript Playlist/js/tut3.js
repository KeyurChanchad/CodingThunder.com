console.log('tut3');
// Variables in js
//There are 3 way to declare variable var, let, const
// var has global scope, let has block scope
var name = 'keyur';
var channel;
var marks = 3454;
marks = 0;
// channel = 'CodeWithKeyur'
console.log(name, channel, marks);

 /* Rules for creating JavaScript Variables
1. Cannot start with numbers
2. Can start with letter, _ or $
3. Are case sensitive
*/
var city = 'Delhi';
console.log(city);

const ownersName = 'Hari Ram';
// ownersName = 'Keyur'; // Cannot do this (error) but destroy program
console.log(ownersName);
const fruit = 'Orange';

//This is block
{
 let city = 'Rampur';   
 city = 'Kolkata';
 console.log(city);
}
console.log(city);


const arr1 = [12, 23, 12, 53, 3];
// arr1.push(45);
console.log(arr1);

/* Most common programming case types:

1. camelCase    keyurChanchad 
2. kebab-case   keyur-chanchad
3. snake_case   keyur_chanchad
4. PascalCase   KeyurChanchad
*/