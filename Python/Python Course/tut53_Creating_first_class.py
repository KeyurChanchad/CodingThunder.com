# Defining a Class in Python
# As in function, definitions begin with the keyword def, class begins with a class keyword.

class MyClass:
    '''This is a docstring.'''
    pass

# Object_name.variable_name = “abc”

# Creating object
# Stu1 = MyClass()
# Stu2 = MyClass()

class Student:
    pass       # pass is noting it simply tell that this class do noting


keyur = Student()
mayur = Student()

keyur.name = "Keyur"
keyur.std = 12
keyur.section = 1
mayur.std = 9
mayur.subjects = ["hindi", "physics"]

print(keyur.section, mayur.subjects)




