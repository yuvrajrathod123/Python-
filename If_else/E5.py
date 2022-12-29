
# write a python program that prints all the number from 0 to 6 expect 3 and 6 (use continue)
# expected output: 0 1 2 4 5

for n in range(6):
    if n == 3 or n == 6:
        continue
    print(n,end=" ")
print("\n")