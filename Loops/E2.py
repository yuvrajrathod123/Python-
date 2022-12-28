
# program to print the following pattern

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


n = int(input("Enter the number line: "))

# for i in range(n):
#     for j in range(i):
#         print("*", end=" ")
#     print("")

# for i in range(n,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print("")


for i in range(10):
    if i<= 5:
        print("*" * (i))
    else:
        print("*" * (n-i))
       