import random
from random import choice
from random import randint
from random import shuffle

# choice function

l1 = [1, 3, 4, 5, 7]
x = choice(l1)
print(x)

# randint function

otp = randint(1000,9999)
print("Your otp: ", otp)

#shuffle function

l2 = ["Apple", "Mango", "Orange", "Banana"]
shuffle(l2)



print("Shuffled list: ",l2)