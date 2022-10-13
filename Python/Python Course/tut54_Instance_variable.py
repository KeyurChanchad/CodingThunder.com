# Instance variable:
"Instance variables are the variables for which the value of the variable is different for every instance."

# Class variable:
# "Class attributes are owned by the class directly, which means that they are not tied to any object or instance."

# "It is worth noting that updating the value of the class variable will not change it for the instance variables of the objects, such as in the case above."

# The __dict__ attribute
# Every object in Python has an attribute which is denoted by __dict__, it maps the attribute name to its value. This dictionary is used to stores all the attributes defined for the object itself. Following is the syntax of using __dict__:
#
# object.__dict__

# ---------------------------------------------------
class Employee:
    no_of_leaves = 8
    pass

keyur = Employee()      # instance declare like this
prashant = Employee()

keyur.name = "Keyur"
keyur.salary = 455
keyur.role = "Instructor"

prashant.name = "Prashant"
prashant.salary = 4554
prashant.role = "Student"


print(Employee.no_of_leaves)
print(Employee.__dict__)     # __dict__ return dictionary of variable of instance or class

Employee.no_of_leaves = 9       # class  can change class variable
print(Employee.__dict__)
print(Employee.no_of_leaves)

# print(keyur.no_of_leaves)
# print(keyur.__dict__)
# keyur.no_of_leaves = 34       # This variable is add in this particular instance or object
# print(keyur.no_of_leaves )
# print(keyur.__dict__)

# print(Employee.no_of_leaves)   # Object can't change class variable
