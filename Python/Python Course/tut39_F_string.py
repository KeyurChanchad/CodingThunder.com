#1 String Formatting (% Operator)
# name="Jack”
#  n = "%s My name is %s” %name
# print(n)
#  Output: "My name is Jack."

#2 Using Tuple ()
# name=”Jack”
# class=5
# s=”%s is in class %d”%(name,class)
# print(s)

#3  String Formatting (str.format)
# Syntax: {}.format(values)
# str = "This article is written in {} "
# print (str.format("Python"))

#4 Using f-Strings ( f ):
# declaring variables
 # str1="Python”
 # str2="Programming”
# print(f"Welcome to our {str1}{str2} tutorial”)

# Time Module:-
# import  time

# F strings
import math

me = "Keyur"
a1 = 3
# a = "this is %s %s"%(me, a1)
# a = "This is {1} {0}"
# b = a.format(me, a1)
# print(b)
a = f"this is {me} {a1} {math.cos(65)}"
# time
print(a)

