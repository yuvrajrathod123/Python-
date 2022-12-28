#FOR LOOPS

         #for(i=10; i>1; i--)
for x in range(10,1,-1):  #Range is used in the loops to control the number of types loop have to run
    print(x)

#Print the hello word 5 time  
for  i in range(0,6):
    print("Hello")

#For loop with strings
print()
for letter in "Python":
    print(letter, end="")  #Here the end is used to avoid the 
                           #next line print the all all letter in one line



# For loop in the list 
print()
li = ["yuvi", "a", 3, "40"]
for x in li:
    print(x)


# Loops in the tuple
print()
tuple_list = {(1,2), (2,3), (3,4)}
for item in tuple_list:
    print(item)

#tuple Unpacking

for(item1, item2) in tuple_list:
    print(item1)
    print(item2)
    print()


#For loop in the dictionary
print()
user = {'name':'yuvi', 'gamil':'yuvi2gmail.com', 'pass':'rathod'}
for item in user:
    print(item)        # it will key

print()
for item in user:
    print(user[item])   # it will  value


#else part in the loop
print()
list = [1, 2, 3, 4] # When the list is empty ( list = [] )in thid case it will print done
for x in list:
    if x == 3:
        break
    print(x)
else:
    print("done")