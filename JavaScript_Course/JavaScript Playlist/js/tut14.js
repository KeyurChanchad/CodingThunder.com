console.log('Welcome to tutorial 14');
/*
element selectors:
1. Single element selector
2. Multi element selector

*/

// 1. Single element selector
let element = document.getElementById('myfirst');
// element = element.className;     //"child red good"
// element = element.childNodes;    //element.children
// element = element.parentNode;   //element.parentElement
// element = element.firstElementChild;
// element = element.lastChilds;
// console.log(element)
element.style.color = 'red';
element.innerText = 'Keyur is a good boy';
element.innerHTML = '<b>Keyur is a very good boy</b>';
// console.log(element.innerText);


// document.querySelector is take either id or class and select on first occurence
// let sel = document.querySelector('#myfirst');
// sel = document.querySelector('.child');
sel = document.querySelector('div');
// sel.style.color = 'green';
// console.log(sel)

// 2. Multi element selector
// let elems = document.getElementsByClassName('child');
// elems = document.getElementsByClassName('container');
elems = document.getElementsByTagName('div');
console.log(elems)

// for (let index = 0; index < elems.length; index++) {
//     const element = elems[index];
//     console.log(element);
//    element.style.color = 'pink'; 
// }

Array.from(elems).forEach(element => {
    console.log(element);
   element.style.color = 'green'; 
});
console.log(elems[0].getElementsByClassName('child'))