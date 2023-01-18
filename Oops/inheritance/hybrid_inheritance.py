

# Hybrid inheritance

class A:
    def myfunction1(self):
        print("Function of claas A")

class B(A):
    def myfunction2(self):
        print("Function of claas B")

class C(A):
    def myfunction3(self):
        print("Function of claas C")

class D(B,C):
    def myfunction4(self):
        print("Function of claas D")

d = D()
d.myfunction1()
d.myfunction2()
d.myfunction3()
d.myfunction4()