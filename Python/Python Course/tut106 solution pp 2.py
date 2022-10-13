apple = int(input("Enter a number of Apple."))
min = int(input("Enter a minimum number."))
max = int(input("Enter a maximum number."))

if min == max:
    print("min and max are equal:")
print("The range is..")

for i in range(min, max+1):
    # print(i, end=" ")
    if apple%i == 0:
        print(f"{i} is divisor of {apple}")
    else:
        print(f"{i} is not divisor of {apple}")
