

# multipal inheriatance

class A :  #1st parent class
    def myfunction1(self):
        print("class a function clalled")

class B :  # 2nd paren class
    def myfunction2(self):
        print("class b function clalled")

class C(A,B) :  #child class
    def myfunction3(self):
        print("class c function clalled")

c1 = C() 
c1.myfunction1()       
c1.myfunction2()       
c1.myfunction3()       