list1 = [ ["Harry", 1], ["Larry", 2],
          ["Carry", 6], ["Marry", 250]]

dict1 = dict(list1)
#convert into dictionary
for key in dict1:
    print(key)

for key, value in dict1.items():
    print(key, "and lolly is ", value)
items = [int, float, "Keyur", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)

