console.log("This is tutorial 34");
// setInterval and setTimeout is non blocking method.  Means it not block the content.

// setTimeout means it work after 10 second. 
setTimeout(() => {
    for (let index = 0; index < 2005; index++) {
        const element = index;
        console.log("This is index number" + index);
    }
}, 10000);

// setInterval means it work after every 3 second. 
// setInterval(() => {
//     console.log('keyur ');
    
// }, 3000);
console.log('done printing');
