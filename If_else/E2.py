

# Program to convert temprature to and from celcius , fahrenheit
# fornula c/5 = (f-32)/9
# c =(5/9)*(f-32)
# f =(c*(9/5) + 32)

option = str(input("Enter c to convert into fahrenheit And f to convert into celsius: "))

if option == "c":
    c = float(input("Enter the temprature in celcius: "))
    far = (c*(9/5) + 32)
    print("The temprature in Fahrenheitn : ",far,"F")

elif option == "f":
     f = float(input("Enter the temprature in Fahrenheitn: "))
     cel = (5/9)*(f-32)
     print("The temprature in Fahrenheitn : ",cel,"C")
else:
    print("Plz Enter right option")