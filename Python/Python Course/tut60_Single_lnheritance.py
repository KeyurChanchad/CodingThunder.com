# "Inheritance is the ability to define a new class(child class) that is a modified version of an existing
# class(parent class)"

# class Parent_class_Name:
# #Parent_class code block
# class Child_class_Name(Parent_class_name):
# #Child_class code block

# class Parent():
#     def first(self):
#         print('Parent function')
#
#
# class Child(Parent):
#     def second(self):
#         print('Child function')
#
# object1 = Child()
# object1.first()
# object1.second()

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)
        # return   # it is returning nothing so it print none

class Programmer(Employee):
    no_of_holiday = 56
    def __init__(self, aname, asalary, arole, languages):
        # it not use we use super() here in ahead
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"

keyur = Employee("Keyur", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Programmer("Shubham", 555, "Programmer", ["python"])
kishan = Programmer("Kishan", 777, "Programmer", ["python", "Cpp"])

# print(kishan.no_of_holiday)
# print(shubham.printdetails())   #base class method
# print(shubham.printgood("I am good boy"))

print(kishan.printprog())
# print(shubham.printprog())

