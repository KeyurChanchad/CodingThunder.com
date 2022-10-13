# '==' is used to represent value equality.
# Value equality means that two variables or objects or even data structures such as list composes of the same value.
# Suppose we have two variables a and b. We assign the value 2 to both of them.
# Now, as we know that they do not have any direct link with each other,
# the only similarity is that they have been given the same value. So, if we place an '==' sign between them,
# the output will be True. However, when we change the value of one of the variables, it will return false.

# For Example:-
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
x == y
#True


# Identity operator (is) in Python:
# 'is' is generally used to denote reference equality. The data structure or variables in the case has to be the same. In the case of the object, the objects must be referring to the same kind of data. In case we use a copy of our variable or data structure or even make a similar one with the same values, it will still return False as their reference is not the same. For example, if we assign a list to two different objects, then the 'is' keyword will return true as they are both referring to the same list. In case we change an entry in the list, it will also be changed for the other one, so no change in output.

# For Example:-
c = [1, 2, 3]
d = [1, 2, 3]
c == d #True
c is d #False



# == - value equality - Two objects have the same value
# is - reference equality - Two references refer to the same object


# Task:
a =[6, 4 , "34"]
b = [6, 4 , "34"]
# print(b is a)
# print(a == b)
c = a
# print(a == c)
# print(a is c)

a  = [ 1,5 ,8]

b =a
a == b
# True
b == a
# True
a is b
# True
b is a
# True
c = [1,5, 8]
a == b
# True
a == c
True

a == c
# True
c ==a
# True
a is c
# False
