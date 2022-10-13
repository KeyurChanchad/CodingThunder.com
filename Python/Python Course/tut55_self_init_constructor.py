# Self keyword:
# The self keyword is used in the method to refer to the instance of the current class we are using. The self keyword is passed as a parameter explicitly every time we define a method.
#
# def read_number(self):
#         print(self.num)


# __init__ method:-
# "__init__" is also called as a constructor in object-oriented terminology. Whereas a constructor is defined as:
#
# "Constructor in Python is used to assign values to the variables or data members of a class when an object is created."

# def __init__(self):
    # body of the constructor

# The def keyword is used to define the function.
# The first argument refers to the current object which binds the instance to the init() method.
# In init() method ,arguments are optional. Constructors can be defined with any number of arguments or with no arguments.

# For Example:
#
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# p1 = Person("John", 36)
# print(p1.name)
# #Output: John


# Types of constructors in Python
# We have two types of constructors in Python.

# 1. The default constructor is the one that does not take any arguments.
# 2. Constructor with parameters is known as parameterized constructor.



class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):    # It is a constructor self is nothing but it is instance or class by whom this function is called
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


keyur = Employee("Keyur", 255, "Instructor")

# krupal = Employee()
# keyur = Employee()

# keyur.name = "Keyur"
# keyur.salary = 455
# keyur.role = "Instructor"
#
# krupal.name = "Rohan"
# krupal.salary = 4554
# krupal.role = "Student"

# print(keyur.salary)
print(keyur.printdetails())



