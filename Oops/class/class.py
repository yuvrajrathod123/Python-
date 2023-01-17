

# creating a class

class bike:
    name = ""
    color = "red"
    
    
# creating an object for thhe bike class

bike1 = bike()

# accesing the attributes of bike class
print(bike1.name) 
print(bike1.color) 

# assign a new values to the attributes of bike clas

bike1.name = "splender"
bike1.color = "green"

# print(bike1.name) 
# print(bike1.color) 

print(f"name: {bike1.name}, color: {bike1.color}")