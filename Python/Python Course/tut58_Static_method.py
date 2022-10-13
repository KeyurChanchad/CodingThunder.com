# class Student:
# @staticmethod
#     def myfunc():
#         //Code to be executed
#
# staticmethod(class_name.method())
# Finally, note that in a static method, we do not need the self or cls to be passed as the first argument.

# NOTE : IF WE WANT TO USE INSTANCE VARIABLE WE USE SELF , WE WANT TO USE CLASS VARIABLE WE USE CLASS METHOD AND
# WE WANT TO USE NOTING NEITHER SELF NOR CLASS THEN STATIC METHOD USE

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
        return cls(*string.split(" "))

    @staticmethod      # static method is a simple method
    def printgood(string):
        print("This is good " + string)

keyur = Employee("keyur", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
kiran = Employee.from_dash("Kiran 480 Student")

Employee.printgood("Keyur")


