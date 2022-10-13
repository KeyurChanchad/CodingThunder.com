# Iterables are objects that can be placed inside a loop and are capable of returning one variable at a time.
# In simple terms, we can say that iterables are objects capable of iteration.
# Examples of iterable include list, string, tuple, etc.

# for c in a:
#       print (a)
#Here a is an iterable.
"""
Now, moving on to iterator. An iteration can be defined as an object that does iterations on iterable.
Meaning that it will move from character to character doing iteration.
Every iterable, either it is a string or tuple has a built-in method __iter__() that creates an object when called.
The object moves from character to character of iterable using the __next__() method.
The __next__() method is, what's really behind the working of the loop.


What are the Generators in Python?
Generators concept is also very similar as it is used to make an iterator. The only difference comes in the return statement.
The generator does not use a return statement.
Instead, it uses a yield keyword. Yield functionality is very similar to return as it returns a value to the caller,
but the difference is that it also saves the state of the iterator.
Meaning that when we use the function again, the yield will resume it is the value from the place it left off.

Generators in Python are created just like the normal functions using the ‘def’ keyword.
Generator functions do not run by their name, and they are run when the __next__() function is called.
Generator is very helpful in projects relating to memory issue because like a simple iterator,
it does not return all the values at a time instead it produces, series of values overtime.
So a generator is generally used when we want to iterate over a series of values but do not want to store them completely in memory.
"""
# def getNum (x):
#     for i in range(x):
#         yield i

# seq = getNum (2)
# print(seq.__next__())
# print(seq.__next__())
# print(seq.__next__())

# Output:
# 0
# 1
# Traceback (most recent call last):
# File "<stdin>", line 7, in <module>
#  print(seq.__next__())
# StopIteration

# When we run print(seq.__next__()) for the third time, StopIteration is raised.
# This is because a for loop takes an iterator and iterates over it using __next__() function which automatically ends when StopIteration is raised.


"""
Iterable - __iter__() or __getitem__()    it is an object that is iterable or not if iterable then use iter or getitem method
Iterator - __next__()          if it iterable then it goes to iterator.we can run next()
Iteration -    It is a process 
generator is getting value on the fly means when it stop from there it start
"""

def gen(n):
    for i in range(n):
        yield i      # if we write return here then it become simple function but yield it generator or iterator

g = gen(3)
# print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(g.__next__())


# for i in g:
#     print(i)     # for loop is auto stop iteration

# h = 546546        'int' object is not iterable
h = "keyur"         # string is iterable
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
# for c in h:
#     print(c)
