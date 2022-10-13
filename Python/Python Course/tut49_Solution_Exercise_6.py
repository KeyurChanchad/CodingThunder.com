# Snack Water Gun
# Create a snake water gun game in python! Search Snake water gun game in google if you need help on rules and how to play the game!

import random
print("Welcome in Snack Water Gun Game:")
i = 1
comcnt = 0
mycnt = 0
drawcnt =0
while (i <= 5):
    print("\n 1.Snack\n 2.Water\n 3.Gun")
    list = ["snack", "water", "gun"]
    ch = int(input("Enter number 1,2,3 for game:"))
    dic = {1:"snack", 2:"water", 3:"gun"}
    print(f"My choice is {dic[ch]}")
    rndch =  random.choice(list)
    print(rndch)

    if (ch == 1 and rndch == "snack"):
        print("Draw....")
        drawcnt+1
    elif(ch ==1 and rndch == "water"):
        print("You win....")
        mycnt+1
    elif(ch ==1 and rndch == "gun"):
        print("Computer win....")
        comcnt+1

    elif (ch == 2 and rndch == "water"):
        print("Draw....")
        drawcnt+1
    elif(ch ==2 and rndch == "gun"):
        print("You win....")
        mycnt + 1
    elif(ch ==2 and rndch == "snack"):
        print("Computer win....")
        comcnt + 1

    elif (ch == 3 and rndch == "gun"):
        print("Draw....")
        drawcnt+1
    elif(ch ==3 and rndch == "snack"):
        print("You win....")
        mycnt + 1
    elif(ch ==3 and rndch == "water"):
        print("Computer win....")
        comcnt+1
    else:
        print("Please insert correct input...")
    i = i+1

if mycnt >= comcnt and mycnt >= drawcnt:
    print("Finally You are winner:")
elif comcnt >= mycnt and comcnt>= drawcnt:
    print("Finally computer is winner:")
else:
    print("Draw....")
