/* 
let str = /Code with Keyur/i;
Here /Code with Keyur/i is a regular expression. "code with Keyur" is a pattern and "i" is a modifier that modifies the search to be case-insensitive. If we write /Code with keyur/g, here “g” performs a global match that will find all matches rather than stopping after the first match.


exec():-
This method will executes a search for a match in a string. It returns an array of information or null on a mismatch. 
let obj = /k/.exec("Code with keyur");


test():-
This method tests for a match in a string. It returns true or false.
let str = /Code/;
str.test("Code with keyur!");

match():-
This method will return an array containing all of the matches, including capturing groups, or null if no match is found. 
let str = "JavaScipt tutorial from begineer to advance level"; 
let result = str.match(/ial/);


search():-
This method will tests for a match in a string. It returns the index of the match, or -1 if the search fails.
let str = 'Code with keyur';
let reg = /od/;
// search if the pattern is in string variable
let result = str.search(reg);
console.log(result); 

replace():-
This method will executes a search for a match in a string, and replaces the matched substring with a replacement substring. 
let str = "Code with abc!";
let result = str.replace("abc", "Keyur");


split():-
This method uses a regular expression or a fixed string to break a string into an array of substrings.
const test = /[\s,]+/;
let result = 'Hello world! '.split(re);
console.log(result); // ["I", "am", "learning", "JavaScript", "RegEx"]
 
*/


console.log("This is tutorial 46");
let reg = /keyur/; // This is a regular expression literal in js
reg = /keyur/g; // g means global
// reg = /keyur/i; // i means case insensitive

// console.log(reg);
// console.log(reg.source);

let s = "This is great code with keyur and also keyur bhai";
// Functions to match expressions
// 1. exec() - This function will return an array for match or null for no match
let result = reg.exec(s);
// result = reg.exec(s);
console.log(result);
// result = reg.exec(s);
// console.log(result); ---> We can use multiple exec with global flag

// if (result) {
//     console.log(result);
//     console.log(result.input);
//     console.log(result.index);
// }

// 2. test() - Returns true or false
let result2 = reg.test(s);
// console.log(result2); // --> This will only print true if the "reg" is there in the string "s"

// 3. match() - It will return an array of results or null
// let result3 = reg.match(s) ---> This is wrong!!
let result3 = s.match(reg) // ---> This is right
// console.log(result3);

// 4. search() - Returns index of first match else -1
// let result4 = reg.search(s) ---> This is wrong!!
let result4 = s.search(reg) // ---> This is right
// console.log(result4);

// 5. replace() - Returns new replaced string with all the replacements (if no flag is given, first match will be replaced)

let result5 = s.replace(reg, 'CHANCHAD');
console.log(result5);

