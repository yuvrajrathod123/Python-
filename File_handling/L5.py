f1 = open("hello.txt",'w')
lines_of_text = ["line 1\n","line 2\n","line 3\n","line 4\n"]
f1.writelines(lines_of_text)

f1 = open("hello.txt",'r')
str = f1.read()
print(str)
f1.close()