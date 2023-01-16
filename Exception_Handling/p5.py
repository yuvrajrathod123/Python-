
# write a program to input a string from the user and check using try and except is it string or not

try:
    a = str(input("enter a string:"))
    print(a)
except Exception as f:
    print("Exception caught:",f)

print("Jml bhava")