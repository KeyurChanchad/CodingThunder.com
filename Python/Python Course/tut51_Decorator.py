# Decorator is used when function is return function or it take function as argument
# Note that a decorator is called before defining a function.

# There are two ways to write a Python decorator:

# We can pass our function to the function as an argument, thus define a function and pass it to our decorator.
#  We can simply use the @ symbol before the function we'd like to decorate.

def inner1(func):
    def inner2():
        print("Before function execution")
        func()
        print("After function execution")
    return inner2

@inner1
def function_to_be_used():
    print("This is inside the function")

function_to_be_used()


# def function1():
#     print("Subscribe now")

# func2 = function1      #function1 in not call  both points same function
# del function1
# func2()

# In python function can return a function
# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
#
# a = funcret(1)
# print(a)

# def executor(func):
#     func("this")
# executor(print)

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")

    return nowexec

@dec1
def who_is_keyur():
    print("Keyur is a good boy")

# who_is_keyur = dec1(who_is_keyur)   #it is same as above

who_is_keyur()     # when it called it see if @dec1 is here means that this function is provide as an agrument to the dec1 fun


