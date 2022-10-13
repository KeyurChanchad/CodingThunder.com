# ABC = abstract base  class
# from abc import ABCMeta , abstractmethod
from abc import ABC, abstractmethod       #both are same python 3.0 above version support this

# class Shape(metaclass = ABCMeta):   # 1.
class Shape(ABC):   #2.
    # A class which has abstract method that inherited then it must be define.  it always declare
    @abstractmethod
    def printarea(self):
        return  0

class Rectengle(Shape):
    type = "Rectengle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 8

    def printarea(self):
        return  self.length * self.breadth

rect = Rectengle()
print(rect.printarea())

# shape1 = Shape()       #Abstract class object can't create