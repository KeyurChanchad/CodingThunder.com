'''
The task you have to perform is “Guess The number”. This task consists of a total of 10 points to evaluate your performance.

 Problem Statement:-
Generate a random integer from a to b. You and your friend have to guess a number between two numbers a and b. a and b are inputs taken from the user. Your friend is player 1 and plays first. He will have to keep choosing the number and your program must tell whether the number is greater than the actual number or less than the actual number. Log the number of trials it took your friend to arrive at the number. You play the same game and then the person with minimum number of trials wins! Randomly generate a number after taking a and b as input and don’t show that to the user.

Input:
Enter the value of a:    4

Enter the value of b:   13

Output:
Player1 :
Please guess the number between 4 and 13
5
Wrong guess a greater number again

8
Wrong guess a smaller number again

6
Correct you took 3 trials to guess the number

Player 2:

Correct you took 7 trials to guess the number

Player 1 wins!
'''


import  random


if __name__ == '__main__':

    # take a range from the user
    a = input("Enter first number of range.     ")
    b = input("Enter second number of range.    ")

    correct_num_player = random.randint(int(a), int(b))
    player_count = 0

    correct_num_my = random.randint(int(a), int(b))
    my_count = 0

    while True:
        print("\nPlayer 1 turn.")
        player_num = int(input(f"Please guess the number between {a} and {b}:    "))
        if player_num > correct_num_player:
            print(f"Wrong!  guess a greater number try again")
            player_count += 1

        elif player_num < correct_num_player:
            print("Wrong guess a smaller number again")
            player_count += 1

        else:
            player_count += 1
            print(f"You took {player_count} trials to guess correct the number")
            break

    while True:
        print("\nNow its your turn.")
        my_num = int(input(f"Please guess the number between {a} and {b}:    "))

        if my_num > correct_num_my:
            print(f"Wrong!  guess a greater number try again")
            my_count += 1

        elif my_num < correct_num_my:
            print("Wrong guess a smaller number again")
            my_count += 1

        else:
            my_count += 1
            print(f"You took {my_count} trials to guess correct the number")
            break

    if my_count > player_count:
        print("\nPlayer 1 is  Winner!")
    elif my_count < player_count:
        print("\nYou are Winner!")
    else:
        print('\n It Draw happened')







