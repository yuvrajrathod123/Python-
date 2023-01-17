
# Python Methods

# We can also define a function inside a Python class.
# A Python Function defined inside a class is called a method

class rectangle:
    length = 0
    breath = 0

    # method to calculate the area
    def area_of_rectangle(self):
        area = self.length * self.breath
        print("Area of a triangle:", area)

# crating object of rectangle class
rectangle1 = rectangle()

# assign values to all the attributes 
rectangle1.length = 5
rectangle1.breath = 10

# access method inside class
rectangle1.area_of_rectangle()