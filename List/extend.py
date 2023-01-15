

# extend()
# This function adds iterable elements to the list.

extend_list = []

extend_list.extend([1,2])  # extending list elements
print(extend_list)

extend_list.extend((3,4))  # extending tuple element
print(extend_list)

extend_list.extend('abc')  # extending string elements
print(extend_list)

# ===============
print()
list1 = [1,2]
list2 = ['a','b']

list1.extend(list2)
print(list1)
