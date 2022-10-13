def sum():
    a = 10  # local variable cannot be accessed outside the function
    b = 20
    sum = a + b
    print(sum)
sum()
# print(a)  # this gives an error

a=1  #global variable
k = 45
# k = k +4
# print(k)
def print_Number():
    print(k)
    # a=a+1     #local variable can not change the value of the global variable
    # print(a)

print_Number()


l = 10 # Global

def function1(n):
    # l = 5 #Local
    m = 8 #Local
    global l      #if you want to change value of global variable than you use global keyword
    l = l + 45
    print(l, m)
    print(n, "I have printed")
#
function1("This is me")
# print(m)

x = 89
def keyur():
    x = 20
# nested function
    def prashant():
        global x
        print("IN prashant fuction before change",x)
        x = 88
        print("in prashant function after " , x)

    print("before calling prashant()", x)
    prashant()
    print("after calling prashant()", x)


keyur()
print(x)






