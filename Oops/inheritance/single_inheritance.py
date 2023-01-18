

# single inheritance

class parentclass:
    def myfunction1(self):  #parent class propert
        print("parent class function called")


class childclass(parentclass):  # child class which inherits parentclass
   def myfunction2(self):
        print("child class function called")

# creating an object of child class

c1 = childclass()
c1.myfunction1()
c1.myfunction2()
