console.log('Welcome to tut 12.js');
let a = document;
// a = document.all;
a = document.body;
a = document.forms[0];
console.log(a);
// Array.from(a).forEach(function(element){
//     console.log(element);
// })
key = document.links;
// use document.images and document.scripts and print the list of images and scripts on an html page
Array.from(key).forEach(function(element, index){
    console.log(index+1, element)
})
