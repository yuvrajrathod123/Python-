

n = int(input("Enter the number: "))
x = 0
y = 1

for i in range(1, n + 1):
    c = x + y
    print(x,end=" ")
    x = y
    y = c
      
   
