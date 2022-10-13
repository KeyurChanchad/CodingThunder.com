
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithkeyur.com"

    def explain(self):
        return  f"This Emplooyee is {self.fname} {self.lname}"

    @property    #  This decorator is use for when we call method email()  function but we call only email attribute then this is use
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set. Please set by setter..."
        return f"{self.fname}.{self.lname}@codewithkeyur.com"

    @email.setter
    def email(self, string):
        print("Setting now....")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None    #In oops we not delete but do none
        self.lname = None


keyur_chanchad = Employee("Keyur", "Chanchad")

# print(keyur_chanchad.lname)
# print(keyur_chanchad.explain())
# print(keyur_chanchad.email)    # this email is attribute

print(keyur_chanchad.email)     # this is email() but by decorator @property declare like email

keyur_chanchad.fname = "Keyurbhai"    # if email is attribute then not change
# print(keyur_chanchad.fname)
print(keyur_chanchad.email)

# First of all it find setter that not presence it show error
# this email() get starting and find that method
keyur_chanchad.email = "this.that@codewithkeyur.com"     #AttributeError: can't set attribute   without setter
# print(keyur_chanchad.fname)

# First of all it find deleter that not presence it show error
del keyur_chanchad.email      #AttributeError: can't delete attribute  without deletter
print(keyur_chanchad.email)