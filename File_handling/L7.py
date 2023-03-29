#  with statement and split method reading an d writing fike content

# with statement

with open("hello.txt","w") as f1:
    f1.write("hwllo world")

with open("hello.txt","r") as f2:
    data = f2.readlines()
    print(data)  

with open("hello.txt","r") as f3:
    data = f3.readlines()
    for line in data:
        words = line.split()
        print(words)            