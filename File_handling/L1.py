
# we use open method to create the file
# open("file name","Permission")

s = "My name is Yuvraj Rathod"
y = "i am currently studing at don bosco institute of technology"

file = open("yuvi.txt","w")
file.write(s)
print("File created")
file.close()


# how to read the file 

file = open("yuvi.txt","r")
filecontent = file.read()
print(filecontent)

# storing list into the file

l1 = ["Apple", "Mango", "Kivi", "Orange", "Gava"]

file = open("Demo.txt","w")
file.writelines(l1)
print("File created22")
file.close()

# reading list from the file

file = open("Demo.txt","r")
filelist = file.readlines()
print(filelist)

# Appending the file means adding some content at last

d = "I love Programming"
file = open("yuvi.txt","a")
file.write(d)
print("file updated")
file.close