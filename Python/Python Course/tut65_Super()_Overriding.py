class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"
    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        super().__init__()
        print(super().classvar1)     # if method is override and we want to access base class variable or method then we use super()


a = A()
b = B()

print(b.classvar1)       # b.classvar1  first find in B class instance variable then A class instance variable then B class class variable then A class class variable
# if class B instance variable not their and A class instance variable is override then then see in Class B class variable

print(b.special, b.var1, b.classvar1)


# class Parent_Class(object):
#     def __init__(self):
#         pass
#
# class Child_Class(Parent_Class):
#     def __init__(self):
#         super().__init__()

