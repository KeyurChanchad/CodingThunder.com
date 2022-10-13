# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
#

print("Enter 1st Number:")
num1 = int(input())
print('Enter 2nd Number:')
num2 = int(input())
print('What do you Want?'+'+,-,/,%,*')
op =input()

if (num1 ==45 and num2==3) or (num1==3 and num2==45) and op=='*':
    print("555")
elif num1 == 56 and num2 == 9 and op == '+':
        print("77")
elif num1 == 56 and num2 == 6 and op == '/':
        print("4")
elif op == '*' :
    num4=num1*num2
    print(num4)
elif op == '+':
    plus=num2+num1
    print(plus)
elif op == '/':
    Dev=num2/num1
    print(Dev)
elif op == '-':
    Dev=num2-num1
    print(Dev)
elif op == '%':
    percent=num2%num1
    print(percent)
else:
    print("Error! Please check your input")
