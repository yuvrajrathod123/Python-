
f1 = open("test.txt","r")
if f1.mode == 'r':
    content = f1.read()
print(content)
print(f1.read(10))

f1 = open("test.txt",'r')
print(f1.readline())
print(f1.readline(3))
print(f1.readlines())