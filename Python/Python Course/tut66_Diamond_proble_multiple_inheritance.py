# In Diamond shape problem python has resolution by order of inheritance

class A:
    def met(self):
        print("I am in class A :")
    pass

class B(A):
    # def met(self):
    #     print("I am in class B :")
    pass

class C(A):
    # def met(self):
    #     print("I am in class C :")
    pass

class D(B, C):
    # def met(self):
    #     print("I am in class D :")
    pass

a = A()
b = B()
c = C()
d = D()

d.met()