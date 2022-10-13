console.log('We are in tut7.js and lets discuss about arrays');
let marks = [34, 23, 24, 93 ,73, 25];
const fruits = ['Orange', 'Apple', 'Pineapple'];
const mixed = ['str', 89, [3, 5], true, 65.26];
// console.log(marks);
// console.log(mixed);
// console.log(fruits[1]);

const arr = new Array(23.56, 123, false, 'Orange');
// console.log(arr.length);
// console.log(Array.isArray('keyur'));
// arr[0] = 'Keyur';
// let arrelement = arr[0];
// console.log('element :', arrelement);
// console.log(arr);

let value = marks.indexOf(73);
// console.log(value)

// Mutating or Modifying arrays
// marks.push(3564);
// marks.unshift(1009);
// marks.pop()
// marks.shift()
// marks.splice(2, 3);   //It remove the elements first is starting index and last is no.of elememt
// marks.reverse()
// marks.sort()
// console.log(marks);

let marks2 = [1, 2, 3, 7]
marks = marks.concat(marks2);
// console.log(marks);

let myobj = {
    'first name': 'keyur', 
    channel: 'CodeWithKeyur',
    isActive: true,
    marks: [1,5,3,6]
}

// console.log(myobj)
// console.log(myobj['channel'])
// console.log(myobj[channel])
// console.log(myobj.channel)
           
