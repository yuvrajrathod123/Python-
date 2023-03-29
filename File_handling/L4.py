f = open("test.txt","w+")
for i in range(10):
    f.write("This is line %d\r\n" %(i+1))    
f.close()

f = open("test.txt",'a+')
for i in range(10):
    f.write("Apended line %d\r\n" %(i+1))
f = open("test.txt",'r')    
str = f.read()  
print(str)  
f.close()