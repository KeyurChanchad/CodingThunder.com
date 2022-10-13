# Syntax:
# class myClass:
#     @classmethod
#     def myfunc (cls, arg1, arg2, ...):
#                           ....
# myfunc defines the function that needs to be converted into a class method
#
# returns: @classmethod returns a class method for function.
#
# Because the class method only has access to cls argument, it cannot modify object instance state.
# However, class methods can still modify class state that applies to all instances of the class. So a class method automatically recognizes a class, so the only parameter that remaines to be passed is the function that needs conversion.
#
# @classmethod Decorator:
#  We have covered decorators in detail in Tutorial #51, so here we are just doing to define the functionality of decorator instead of its working. A @classmethod Decorator is a built-in function in Python. It can be applied to any method of the class. We can change the value of variables using this method too.

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    # class method is used for change the class variable and if we want not use self then it use
    @classmethod
    def change_leaves(cls, newleaves):    # cls is class
        cls.no_of_leaves = newleaves

keyur = Employee("Keyur", 255, "Instructor")
ronak = Employee("Rohan", 455, "Student")


# print(keyur.printdetails())
# Employee.no_of_leaves = 34    # it change class variable it it not recommended
ronak.change_leaves(34)
print(ronak.no_of_leaves)
print(keyur.no_of_leaves)