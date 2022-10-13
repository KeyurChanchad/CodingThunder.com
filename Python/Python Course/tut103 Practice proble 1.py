"""
The task you have to perform is “Your Age In 2090”. This task consists of a total of 10 points to evaluate your performance.

Problem Statement:-
Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).

Here are a few instructions that you must have to follow:

Do not use any type of modules like DateTime or date utils. (-5 points)
Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
Your code should handle all sort of errors like:                       (2 points)
You are not yet born
You seem to be the oldest person alive
You can also handle any other errors, if possible!
"""
while True:
    age =  input("Enter you age or year of birth: ")
    length = len(age)
    # print(length)
    # print( int(age) )

    if age.isdigit():
        if length == 4 and int(age) < 2021:
            yob =  int(age)
            print(f"After {100 - (2021 - int(age))}  years later you will turn 100 years old.")
            print(f"You will be 100 Year old at {100 + int(age) } year.")
            break

        elif length > 0 and length < 4:
            yob = 2021 - int(age)
            print(f"After {100 - int(age)} years later you will turn 100 years old.")
            print(f"You will be 100 Year old at {100 + int(age)} year.")
            break

        else:
            print("Enter valid digit:")

    else:
        print("Enter digit/s ....")
        continue

ch = input("Would like to continue. yes or no: ")
if ch == 'yes':
    year = int(input("Enter year in future to know your age."))
    if len(str(year)) == 4:
        print(f"Your age in {year} is {year - yob } ")
else:
    exit()


