// window.localStorage – It stores the data with no expiration date
// window.sessionStorage -It stores the data for one session. That means the data is lost when the browser tab is closed.

console.log('This is tut 20');
let impArray = ['Gingar, Onion', 'Ladies Finger, Ridge Gaurd'];

// // Add a key-value pair inside local Storage
// localStorage.setItem('key', 'value')
localStorage.setItem('Name', 'Keyur');
localStorage.setItem('Village', 'Khalpar');
// JSON.stringify convert array into string because of localStorage not store array
localStorage.setItem('Vegetable', JSON.stringify(impArray));

// Clears the entire local storage
// localStorage.clear();

// Clear a particular key-value pair
// localStorage.removeItem('Name2');

// Retrieve an item from the local Storage
let name = localStorage.getItem('Name');
name = JSON.parse(localStorage.getItem('Vegetable'));  //converted in array json.parse
// console.log(name)

sessionStorage.setItem('sessionName', 'sKeyur');
sessionStorage.setItem('sessionSirname', 'sChanchad');
sessionStorage.setItem('sessionVegetable', JSON.stringify(impArray));


/* 
let key = 'Entry_1';
localStorage.setItem(key, 'Value');
let myItem = localStorage.getItem(key);
localStorage.setItem(key, 'New Value');
localStorage.removeItem(key);
localStorage.clear();

// Create item:
let myObj = { name: 'Keyur', language: 'JavaScript' };
localStorage.setItem(key, JSON.stringify(myObj));
// Read item:
let item = JSON.parse(localStorage.getItem(key));

*/