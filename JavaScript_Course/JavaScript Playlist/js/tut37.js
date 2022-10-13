// function fun1(){
//    console.log("Code With Harry");
//  }
// function fun2(){
//    console.log("JavaScript Tutorial");
//  }
// fun1();
// fun2();

// function myMessage (str) {
//     setTimeout(() => {
//         // script to download the picture here
//         console.log(`Code With Me`);
//     }, 5000);
// }

// function addition(x, y , callback){
//      setTimeout(() => {
//      document.write(`The sum of ${x} and ${y} is ${x+y}.`);
//      callback();
//       }, 5000);
//  }
// display() function is called just after the ending of addition() function
// function display(){
// document.write('Numbers added!');
//  }
//  // Calling addition() function
// addition(5,5,display);

console.log("This is tutorial 37");

// Pretend that this response is coming from the server
const students = [
  { name: "Keyur", subject: "JavaScript" },
  { name: "kumar", subject: "Machine Learning" },
];

function enrollStudent(student, callback) {
  setTimeout(function () {
    students.push(student);  //students is array
    console.log("Student has been enrolled");
    callback();
  }, 1000);
}

function getStudents() {
  setTimeout(function () {
    let str = "";
    students.forEach(function (student) {
      str += `<li> ${student.name}</li>`;
    });
    document.getElementById("students").innerHTML = str;
    console.log("Students have been fetched");
  }, 3000);
}

let newStudent = { name: "Sunny", subject: "Python" };
enrollStudent(newStudent, getStudents);
// getStudents();
