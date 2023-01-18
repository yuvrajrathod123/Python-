

# multiple inheritance

class A:
    def myfunction1(self):
        print("class a function called")

class B(A):
    def myfunction2(self):
        print("class b function called")

class C(B):
    def myfunction3(self):
        print("class c function called")


c1 = C()

c1.myfunction1()    
c1.myfunction2()    
c1.myfunction3()    