
import time
from functools import lru_cache


@lru_cache(maxsize=3)     # maxsize is how many latest data have you store in cache memory
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n
"""
 latest 3 value of a = some_work()  1, 6, 2 is store in cache memory 
 and whenever b = some_work() is called b is finding value in cache if it there then directly return it not take time
 if b is finding it no there value that store in cache  this some_work() take time which is not there in cache memory
"""
if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)                #
    some_work(6)
    some_work(2)
    print("Done... Calling again")
    # input()
    some_work(6)
    some_work(2)
    some_work(1)
    print("Called again")

# @functools.lru_cache(maxsize=4)
# def myfunc(x):
#     time.sleep(2)
#     return x
#
# myfunc(1)
# # myfunc(1) takes 2 seconds and results for myfunc(1) are now cached
# myfunc(1)
# myfunc(2)
# myfunc(3)
# myfunc(4)
# myfunc(5)


