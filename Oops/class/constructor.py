

# Python constructor

class bike:
    color = ""
    name = ""

    def __init__(self,color,name):
        self.color = color
        self.name = name
        print("color of bike:",self.color)
        print("name of bike:",self.name)

bike1 = bike("red","splender")
      