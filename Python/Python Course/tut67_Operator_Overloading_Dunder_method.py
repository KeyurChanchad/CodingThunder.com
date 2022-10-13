# Mapping Operators  to Function search in google python documentation
# A method  startswith __ and endswith __ it is Dunder method. Dunder method is special method
# Dunder method not always do Operator Overloading but as well as repr and str
class Employee:
    no_of_leaves = 8

    # It is Dunder init special method constructor
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    def __add__(self, other):
        # return  250
        # print(self.salary)
        return self.salary + other.salary


    def __truediv__(self, other):
        return  self.salary / other.salary

    def __repr__(self):
        # return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
        # return  self.printdetails()
        # return "keyur is a good boy"
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"   # generally repr is use for this type message

    # First priority is for __str__
    #--str-- is used for where objectName is show insted of this str method show
    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


emp1 = Employee("Keyur", 345, "Programmer")
emp2 = Employee("Naimish", 96, "clerk")


# This is + operator overloading
# print(emp1 + emp2)

# This is / operator overloading
# print(emp1 / emp2)

# print(emp)
# Output    <__main__.Employee object at 0x000001F9CFB80D90>  without __repr__ and __str__

# print(emp1)    # First priority is for __str__
print(str(emp1))   # Obviously it call __str__ if str there if str not there then print repr
# print(repr(emp1))       # Obviously it call __repr__

print(emp2.__str__())

