grocery = ["Harpic", "vim bar", 92.2,"deodrant", "Balaji", 46]
# print(grocery)
# print(grocery[2])
# print(grocery.sort())     #Error! it is mix
# print(len(grocery))

numbers= [2, 5, 9, 4, 8]
# print(numbers)
# print(numbers[3])

# these function are change original list
# numbers.sort()
# numbers.reverse()
# print(numbers)

# these are slice and not change original list
# print(numbers[0:6])
# print(numbers[:6])
# print(numbers[0:])
# print(numbers[:])
# print(numbers[1:4])

# print(numbers[::-2])
# print(numbers[::-3])
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))

numbers.append(7)   #it insert at the end
numbers.append(26)
numbers.append(7)
# print(numbers)
numbers.insert(1, 99)        #it insert at any index
numbers.remove(5)           #it remove by element
numbers.pop()               #it remove at the ends
print(numbers)
print("--------")
# print(numbers.__contains__(7))
# print(numbers.count(7))

# numbers.clear()
# print(numbers)

# Mutable --- can change
# Immutable ---- cannot change

# list []   ----- mutable
# tuple() ----  immutable

print("Before ", numbers)
numbers[1] = 55   # it changed by this
print("After ", numbers)

tp = (1, 5, 6, 4, 2, 5)
print(tp.count(5))
print(tp)
# tp(1) = 8   error
# tuple = (1)
tuple = (1,)
print(tuple)

a =1
b= 6
# tmp = a
# a = b
# b  = tmp

a, b = b, a
print(a , b)

