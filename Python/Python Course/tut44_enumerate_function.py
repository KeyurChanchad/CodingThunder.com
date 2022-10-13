# enumerate(iterable, start=0)
# When calling a simple enumeration function, we have to provide two parameters:
# ---The data structure that we want to iterate
# ---The index from where we want to start our iteration. By default enumerate function start with 0
# enumerate function return tuple in side list

list_1=["Programing", "with", "Keyur"]
for index,val in enumerate(list_1):
    print(index,val)
##output
# 0 Programing
# 1 with
# 2 Keyur

list_2 = ["Python", "Programming", "Is", "Fun"]
#Counter value starts from 5
result =  enumerate(list_2, 5)
print(list(result))
##output
# [(5, 'Python'), (6, 'Programming'), (7, 'Is'), (8, 'Fun')]


l1 = ["Bhindi", "Aloo", "chopsticks", "chowmein"]

i = 1
for item in l1:
    if i%2 is not 0:
        print(f"Jarvis please buy {item}")
    i += 1

for index, item in enumerate(l1):
    if index % 2 == 0:
        print(f"Jarvis please buy {item}")



