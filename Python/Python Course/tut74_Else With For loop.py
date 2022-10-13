# in for loop if it exit stating to end then else part not exit
# in loop there is a break statment here then else part executed
khana = ["roti", "Sabzi", "chawal"]

for item in khana:
    if item == "roti":
        print(" Koi e mil gaya")
        break
else:
    print("Your item was not found")

"""
for x in n:
   #statements
 else:
   #statements
   
   for i in ['C','O','D','E']:
        print(i)
    else: 
        print("Statement successfully executed")

OUTPUT:
C
O
D
E
Statement successfully executed

In the code above, we iterate over the list and print each element.
 Since we let the loop complete normally, the else statement also executed and "statement successfully executed" is printed. 
 Conversely, if we stop the loop by using the break statement, then the else block will not execute.

"""


for i in range(1, 11):
    if i == 2 :
        print("noting anything")
        break
    print(i)
else:
    print("hy fy")