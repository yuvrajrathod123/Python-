
class animal:  #abstraction class
    def move(self):   #abstraction method
        pass

class dog(animal):
    def move(self):   #class animal impliment method here
        print("i can bark")    

class snake(animal):
    def move(self):   #class animal impliment method here
        print("i can hisss")

d = dog()
s = snake()

d.move()
s.move()
