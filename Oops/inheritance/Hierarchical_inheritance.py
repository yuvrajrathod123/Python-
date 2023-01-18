

# hierarcical inheritance

class A:
    def myfunction1(self):
        print("Class a function called")
class B(A):
    def myfunction2(self):
        print("Class b function called")
class C(A):
    def myfunction3(self):
        print("Class c function called")

b = B()        
c = C()      

b.myfunction1()
b.myfunction2()

c.myfunction1()
c.myfunction3()
