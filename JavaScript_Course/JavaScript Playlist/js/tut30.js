console.log("This is tutorial 30");

const proto = {
    slogan : function () {
        return `This company is the best`;
    },
    changeName : function (newName) {
        this.name = newName
    }
}

// This creates harry object
let keyur = Object.create(proto);
keyur.name = "Keyur";
keyur.role = "Programmer";
// keyur.changeName("chanchad")
// console.log(keyur)

// This also creates harry object
const keyur1 = Object.create(proto, {
    name : { value : "Keyur", writable: true },
    role : { value: "Programmer" },
});
harry1.changeName("keyur2")
// console.log(harry1)


// Employee constructor
function Employee(name, salary, experience) {
    this.name = name;
    this.salary = salary;
    this.experience = experience;
}

// Slogan
Employee.prototype.slogan = function () {
    return `This company is the best. Regards, ${this.name}`;
}

// Create an object from this constructor now
let keyurObj = new Employee("Keyur", 345099, 87);
console.log(keyurObj.slogan())

// Programmer
function Programmer(name, salary, experience, language) {
    Employee.call(this, name, salary, experience);
    this.language = language;
}

// Inherit the prototype
Programmer.prototype = Object.create(Employee.prototype);

// Manually set the constructor
Programmer.prototype.constructor = Programmer;

let rohan = new Programmer("Rohan", 2, 0, "Javascript");
console.log(rohan);


