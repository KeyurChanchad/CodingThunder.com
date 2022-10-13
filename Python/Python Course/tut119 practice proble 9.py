
'''
Problem Statement:-
It's result day at school and not everyone is happy. You decided to make your friends laugh by jumbling their names to come up with some funny names.

Your program should take the number of names and the names separated by space as input. Output should be funny names in the same order.

Input:
Enter number of friends:
3
Enter the name of your 3 friends:
Rohan Das
Shubham Agarwal
Ritesh Arora

Output:
Ritesh Das
Shubham Arora
Rohan Agarwal
'''

size = int(input("Enter number of friends."))

names = [input(f"Enter {i+1} friend's name.") for i in range(size)]
print(names)

new_names = [name.strip().split() for name in names]
print(new_names)

latest_names = new_names.copy()
latest_names.reverse()
print(latest_names)

