
# write a python program to find those number which are divisible by 7 and multiple of 5 between (1500 to 2700) both included

# for x in range(1500,2701,1):
#     if x%7==0 and x%5==0:
#         print(x, end=" ")
    # else:
    #     print("not found")

# by while

# n = 1500

# while n < 2701:
  
#     if n%7==0 and n%5==0:
#          print(n, end=" ")
#     n = n + 1


# in single lilne

print([n for n in range(1500,2700) if n%7==0 and n%5==0])   