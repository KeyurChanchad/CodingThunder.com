"""
Problem Statement:-
You are given a list that contains some numbers. You have to print a list of next palindromes only if the number is greater than 10; otherwise, you will print that number.

Input:
[1, 6, 87, 43]

Output:
[1, 6, 88, 44]

"""
def next_palindrome(n):
    n += 1
    while not is_palindrome(n):
        n += 1
    return n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    # Take size of list from User
    size = int(input("Enter the size of list."))

    # Initialize a blank list
    pp5 = []

    # Add number in blank list
    for i in range(size):
        num = int(input("Enter number one by one."))
        pp5.append(num)

    print(pp5)

    # for num in range(size):
    #     if pp5[num] > 10:
    #         print(f"The next palindrome of {pp5[num]} is {next_palindrome(pp5[num])}.")

    # [print(f"The next palindrome of {pp5[num]} is {next_palindrome(pp5[num])}.") for num in range(size)  if pp5[num] >10]
    new_lst = []
    [new_lst.append(num)  if num < 10 else {new_lst.append(next_palindrome(num))}  for num in pp5]
    print(new_lst)

