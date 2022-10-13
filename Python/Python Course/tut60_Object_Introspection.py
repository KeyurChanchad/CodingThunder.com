# Object Introspection is nothing but it show list of the attributes , methods and which are methods and attrubutes          run for that


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithkeyur.com"

    def explain(self):
        return  f"This Emplooyee is {self.fname} {self.lname}"

    @property
    #  This decorator is use for when we call method email()  function but we call only email attribute then this is use
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set. Please set by setter..."
        return f"{self.fname}.{self.lname}@codewithkeyur.com"


skillf = Employee("skill", "F")

# print(skillf.email)
# print(type(skillf))
# print(type("this is a string"))
print(id("this is string for id"))    # id is unique
print(id("keyur chanchad"))

k = "Keyur is a programmer"
# dir is used for which method and attribute are use there is builtin and created
# print(dir(k))
# dict is used for class and instance it show variables
# print(skillf.__dict__)

print(dir(skillf))

# import inspect
# print(inspect.getmembers(skillf))