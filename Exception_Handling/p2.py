
# Exception while dividing by 0

# a = int(input("Enter the value of A:"))
# b = int(input("Enter the value of B:"))

# c = a/b

# print("Answer:",c)

# print("bye")

# so how to solve this exception

try:  # the code wriiten in try block there can occur error while runtime
    a = int(input("Enter the value of A:"))
    b = int(input("Enter the value of B:"))

    c = a/b

    print("Answer:",c)
except Exception as e:  # htis will run when exception ocuur
    print("Exception caught:",e)

print("bye")