
# Count the number of even and odd from the series of number

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]

even = 0
odd = 0

for num in my_list:
    if num % 2 == 0:
        even = even + 1
    else: 
        odd = odd + 1
           
print("Even: ",even)
print("Odd: ", odd)