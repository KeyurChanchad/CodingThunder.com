/* 
let myPromise = new Promise(function(resolve, reject) {
// code here
});

var mypromise = new Promise(function(resolve, reject) { 
  const x = "geeksforgeeks"; 
  const y = "geeksforgeeks";
  if(x === y) { 
    resolve(); 
  } else { 
    reject(); 
  } }); 
mypromise.then(function(){ 
console.log('Success, You are a GEEK');}).catch(function () { 
console.log('Some error has occurred');}); 


*/

// Promise: Best video on promises
// -resolve
// -reject
// -pending

function func1() {
    // return 'keyur';
  return new Promise(function (resolve, reject) {
    setTimeout(() => {
      const error = true;
      if (!error) {
        console.log("Function: Your promise has been resolved");
        resolve();
      } else {
        console.log("Function: Your promise has not been resolved");
        reject("Sorry not fulfilled");
      }
    }, 2000);
  });
}

func1()
.then(function () {
    console.log("Harry: Thanks for resolving");
  })
  .catch(function (error) {
    console.log("Harry: Very bad bro. Reason: " + error);
  });
