

k = [0,1,2,3,4,5,6,7,8,9]
new_list = []

for i in k:
    if i%2==0:
        new_list.append(i)
print(new_list)

# the same code by the list comprehension

m = [i for i in range(10) if i%2==0]
print(m)