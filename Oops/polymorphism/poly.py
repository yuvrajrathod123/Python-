

class cat:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"i am a cat. my name is {self.name} and my age is {self.age}")    

    def make_sound(self):
        print("meawo")    


class dog:  

    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"i am a dog. my name is {self.name} and my age is {self.age}")    

    def make_sound(self):
        print("bhauu")          

cat1 = cat("mini",2)      
dog1 = dog("pandu",3)  

# cat1.info()
# cat1.make_sound()

for animal in (cat1, dog1):
    animal.make_sound()
    # animal.info()
    # animal.make_sound()
