
# reading and writing files

fl1 = open("file1.txt",'w')           #open the file
fl1.write("i like python.\n not java \n")  

fl1 = open("file1.txt",'r')           #open the file
str = fl1.read(10)
print("Output string is:",str)

fl1.close()  