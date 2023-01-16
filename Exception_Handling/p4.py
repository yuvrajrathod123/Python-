

# User define exception

class MyException(Exception):
    pass

c = int(input("Enter a number:"))
if c > 5:
    raise MyException("Chukla re bhooooo")
else:
    print("Barobar ahe tuz bhavvva")    