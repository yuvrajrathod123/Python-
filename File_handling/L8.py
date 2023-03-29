
fl2 = open("file1.txt",'r+')
str = fl2.read(10)
print("output string is:", str)

# check current position
position = fl2.tell()
print("current pos:", position)

# repositon pointer
position = fl2.seek(0,1)
str = fl2.read(10)
print("after reposition")
print("output string is:", str)
fl2.close