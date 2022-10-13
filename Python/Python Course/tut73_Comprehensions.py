# List as ordinarily are written as such:
# listA = []
# for a in range(50):
#     if a % 5 == 0:
#         listA.append(a)

# While it can be written in a one liner format using comprehension as such:
# listA = [a for a in range(50) if i%5==0]

# alpha = {alpha for alpha in ["a", "a", "b", "c", "d", "d"]}
# The output will be: {'a', 'b', 'c', 'd'}

# Normaldict = {
#   0 : "item0",
#   1 : "item1",
#   2 : "item2",
#   3 : "item3",
#   4 : "item4",
# }
# Compdict = {i:f"Item {i}" for i in range(5)}
#
#
# def gener(n):
#     for i in range(n):
#         yield i
#
# a = gener(5)
# print(a.__next__())
#
# gener = (i for i in range(n))
# a = gener(5)
# print(a.__next__())

# ````````````````````````````````````````````````````````````````````````````
# Comprehersion is a one linear statement for an python object

# 1. List comprehension
# ls = []
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
#
# lst = [i for i in range(100) if i%3==0]
# # in this ls print statement looping statement condition statement
# print(ls)
# print(lst)

# 2.Dictionary comprehension
# dict1 = {i:f"item {i}" for i in range(1, 10001) if i%100==0}
# dict1 = {i:f"Item {i}" for i in range(5)}     # condition is optional

# dict2 = {value:key for key,value in dict1.items()}
# print(dict1,"\n", dict2)

# 3. Generator comprehension
# dresses = (dress for dress in ["dress1", "dress2","dress1",
#                                "dress2","dress1", "dress2"])
# print(type(dresses))
# print(dresses.__next__())
# evens = (i for i in range(10) if i%2==0)
# print(evens.__next__())

# for item in evens:
    # print(item)

# 4. Set comprehension
# alpha = {alpha for alpha in ["a", "a", "b", "c", "d", "d"]}
# print(alpha)
# The output will be: {'a', 'b', 'c', 'd'}


