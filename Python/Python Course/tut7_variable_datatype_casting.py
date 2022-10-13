var1 = "Keyur "
var2 = 26
var3 = 25.2
var4 = "Chanchad"
var5 = "32"
var6 = "8"

print(type(var5))
print(type(var2))
print(var1 + var4)      #Two string are concact
print(var2 + var3)      # two numbers are add
# print(var1 + var2)      error
# print(var5 + var6)
print(int(var5) + int(var6))
"""   
Casting
str()
int()
float()
"""

print(10 * "keyur Boss\n")
print(10 * str(int(var5) + int(var6)) )

print("Enter Your Number: ")
intnum = input()    # input function take argument as a string
print("You entered ", int(intnum) + 10)

print("Enter First Number")
n1 = input()
print("Enter Second Number")
n2 = input()
print("Sum of these two numbers are ", int(n1) + int(n2))


