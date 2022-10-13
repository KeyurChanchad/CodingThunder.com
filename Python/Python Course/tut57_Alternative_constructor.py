
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
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))


krupal = Employee("Krupal", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
keyur = Employee.from_dash("keyur-480-Student")

print(keyur.no_of_leaves)
print(keyur.name)
# rohan.change_leaves(34)
#
# print(krupal.no_of_leaves)

# text = "Python tutorial for absolute beginners."
#  st = text.split()      split return list
#  print(st)


# Example of Class methods - alternative constructor:
# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     @classmethod
#     def from_dash(cls,string):
#
#           return cls(*string.split("-"))
#
# date1=Date.from_dash("2008-12-5")
# print(date1.year)
# #Output: 2008