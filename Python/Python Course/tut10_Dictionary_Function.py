# Dictionary is noting but key value pairs

d1 = {}   # () / []
# print(type(d1))

d2 = {"keyur":"Burger", "ronak":"Roti", "nayan":"mohanthal", "sudani" : {"B":"maggie", "L":"roti", "D":"Bhajiya"}}
print(d2)
# print(d2["keyur"])
# print(d2["sudani"])
# print(d2["sudani"]["B"])

# d2["Akbar"] = "khichadi"
# d2[420]= "junk food"
# del d2[420]
# print(d2)

# d3 = d2
# del d3["keyur"]
# print(d2)

d3 = d2.copy()
del d3["keyur"]      # error if keyur is already deleted
print(d2)

print(d2.get("keyur"))
d2.update({"leena":"Toffee"})
print(d2)

print(d2.keys())
print(d2.items())
print(d2.values())




