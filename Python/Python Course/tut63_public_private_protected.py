
# Public -
# Protected -
# Private -

class Employee:
    no_of_leaves = 8    # Public variable declare like this
    var = 8
    _protec = 9     # Protected variable declare as _var
    __pr = 98       # Private variable declare as __var

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

emp = Employee("Keyur", 343, "Programmer")
# print(emp.var)      # It is accessible at all inside class, derivaed class, sub derived class, outside class because of it is public

print(emp._protec)      # It is accessible inside class, derivaed class, sub derived class because of  it is protected

#private var access by instance.classname.variable : like this
print(emp._Employee__pr)       # It is accessible inside class because of it is private


# Example of public access modifier:
# class employee:
#       def __init__(self, name, age):
#             self.name=name
#             self.age=age

# Example of protected access modifier:
# class employee:
#       def __init__(self, name, age):
#             self._name=name # protected attribute
#             self._age=age # protected attribute

# Example of private access modifier:
# class employee:
#       def __init__(self, name, age):
#             self.__name=name # private attribute
#             self.__age=age # private attribute