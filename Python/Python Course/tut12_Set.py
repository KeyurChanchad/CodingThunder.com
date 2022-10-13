# Set consider Unique value in ascending order
s = set()

# print(type(s))
# s_from_list = set([1, 2, 3, 4, 5])
k = [1, 2, 3, 4, 5]
s_from_list = set(k)
# print(type(s_from_list))
print(s_from_list)

# set take unique value that why it differ from the list, tuple
s.add(1)
s.add(1)
s.add(5)
s.add(4)
print(s)
# s.remove(5)
# print(s)

# s1 = s.intersection({1, 3, 4})
# print("intersection of s and 1,3,4 ", s1)

# s1 = s.union({1, 2, 4})
# print("Union of s and 1,3,4 ",  s1)

# s1 = {4, 6}
# print(s.isdisjoint(s1))

# print(len(s))
# print(max(s))
# print(min(s))

mylist = ([1, 23.2 , 'keyur'])
print(type(mylist))

mytuple = (1, 23, 12, "le")
print(type(mytuple))

# set expected at most 1 argument, so we give one list, tuple, dict
myset = set((1, 15, 45))
print(type(myset))