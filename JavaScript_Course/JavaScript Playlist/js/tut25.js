console.log('This is tutorial 25')
/*
You have to create a div and inject it into the page which contains a heading.
whenever someone clicks on the div, it should be converted into an editable item. whenever user clicks away (blur). save the note into the local storage.

*/

// Create a new element
let divElem = document.createElement('div');

// Add text to that created element
let val = localStorage.getItem('text');
let text;
if (val==null){
 text = document.createTextNode('This is my element. click to edit it');
}
else{
    text = document.createTextNode(val);
}
divElem.appendChild(text);

// Give element id, style and class
divElem.setAttribute('id', 'elem');
divElem.setAttribute('class', 'elem');
divElem.setAttribute('style', 'border:2px solid black; width: 154px; margin: 14px; padding:23px; color:blue');

// Grab the main container
let container = document.querySelector('.container');
let first = document.getElementById('myfirst');


// Insert the divElem before first in container
container.insertBefore(divElem, first);   //insertBefore(insertElement, BeforethisElement)

// console.log(divElem, container, first)

// add event listener to the divElem
divElem.addEventListener('click', function () {
    let noTextAreas = document.getElementsByClassName('textarea').length;  //if edit first time than length 0
    if(noTextAreas == 0){
    let html = elem.innerHTML;
    divElem.innerHTML = ` <textarea class="textarea form-control" id="textarea" rows="3"> ${html}</textarea>`;
    }
    //listen for the blur event on textarea
    let textarea = document.getElementById('textarea');
    textarea.addEventListener('blur', function() {
        elem.innerHTML = textarea.value;
        localStorage.setItem('text', textarea.value);
    })
});

 