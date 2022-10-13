/* 
The Async Keyword:-

async function name(param1, param2, ...paramN) {
    // statements
}

Example: Async function
// async function example
async function func() {
    console.log('Async/Await tutorial.');
    return Promise.resolve(1);
}
func();

async function func() {
    console.log('Async/Await tutorial.');
    return Promise.resolve(1);
}
func().then(function(res) {
    console.log(res)
});

The await keyword:-
The await keyword is used to wait for the asynchronous operation. This keyword is used inside the async function. Here is the syntax to use await is:

let result = await promise;

async function func1() {
let promise = new Promise((resolve, reject) => {
setTimeout(() => resolve("Done with Async/Await!"), 1000)
});
let result = await promise; // wait until the promise resolves 
console.log(result);
}
f();
*/

console.log("This is tutorial 43");
// This funtction is asycronously work non blocking method
async function keyur(){
    console.log('Inside keyur function');
    // data is not fetch untill wait means await 
    const response = await fetch('https://api.github.com/users');
    console.log('before response');
    const users = await response.json();
    console.log('users resolved')
    return users;

    // return "keyur";
}

console.log("Before calling keyur")
let a = keyur();
console.log("After calling keyur")
console.log(a);
a.then(data => console.log(data))
console.log("Last line of this js file")
