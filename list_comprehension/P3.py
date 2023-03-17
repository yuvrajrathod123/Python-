
# 

bits = [True,False,False,True,True,True,False,False]
new_bits =[]

for i in bits:
    if i == True:
        new_bits.append(1)
    else:
        new_bits.append(0)

print(new_bits)

#  lest derive the same output by the list comprehwnsion

m =[1 if i == True  else 0 for i in bits]
print(m)