
# Exception in input

# here if the user enter the string instant number then then it will give exception error
# a = int(input("enter a number:"))
# print(a)
# print("bye")

# so how to this exception lets see

try:
    a = int(input("enter a number:"))
    print(a)
except Exception as e:
    print("Exception caught:",e)

print("bye")
