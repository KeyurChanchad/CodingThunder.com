console.log('Welcome to tutorial 15');

let cont = document.querySelector('.no');
cont = document.querySelector('.container');
let nodeName = cont.childNodes[1].nodeName;   //H1
let nodeType = cont.childNodes[1].nodeType;    //1
// console.log(nodeName)
// console.log(nodeType)
// Node types
// 1. Element
// 2. Attribute
// 3. Text Node
// 8. Comment
// 9. document
// 10. docType

// console.log(cont.childNodes);   //childNodes take text(\n new line) element, comment everything
// console.log(cont.children);      //children take only element

let container = document.querySelector('div.container');

// console.log(container.children[1].children[0].children);

// console.log(container.firstChild);  //text
// console.log(container.firstElementChild);  //h1

// console.log(container.lastChild);
// console.log(container.lastElementChild);
// console.log(container.children);
// console.log(container.childElementCount); // Count of child elements

console.log(container.firstElementChild.parentNode);
console.log(container.firstElementChild.nextSibling);
console.log(container.firstElementChild.nextElementSibling);
console.log(container.firstElementChild.nextElementSibling.nextElementSibling);

