# A number or string when it reversed it look as original number or string that is palindrome
'''
Author: Keyur chanchad
practice proble solution
'''
def next_palindrome(n):
    n += 1
    while not is_palindrome(n):
        n += 1
    return  n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

num = int(input("How many number do you want to Palindrome"))
lst = []
for i in range(num):
    lst.append(int(input("Enter a palindrome number or string:")))

if is_palindrome(lst[i]):
    print(f"{lst[i]} is a palindrome")

for i in range(num):
    print(f"The Next palindrome of {lst[i]} is {next_palindrome(lst[i])}")

# print(lst)



# def next_palindrome(n):
#     n = n+1
#     while not is_palindrome(n):
#         n += 1
#     return n
#
#
# def is_palindrome(n):
#     return str(n) == str(n)[::-1]
#
#
# if __name__ == "__main__":
#     n = int(input("Enter the number of test cases\n"))
#     numbers = []
#     for i in range(n):
#         number = int(input("Enter the number:\n"))
#         numbers.append(number)
#
#     for i in range(n):
#         print(f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")

