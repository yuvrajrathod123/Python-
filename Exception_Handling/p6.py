
# write a program to input two number from the user and check its an integer or not using try
# and except if number are interger then print sum of that number using finally blolck



try:  # the code wriiten in try block there can occur error while runtime
    a = int(input("Enter the value of A:"))
    b = int(input("Enter the value of B:"))

    c = a+b
    print("Sum of two numbers:",c)

except Exception as e:  # this will run when exception ocuur
    print("Exception caught:",e) 

finally:
    # c = a+b
    print("Sum of two numbers:")

print("bye")    