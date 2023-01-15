

# insert()
# This function adds an element at the given index of the list.

list = [1,2,3,4,5,6]

print("current number list:",list)

num = int(input("Enter the number to be insert:"))
index = int(input("Enter the index where you want insert the number "))

list.insert(index,num)

print("updated list:",list)