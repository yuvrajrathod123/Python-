

# write a program that accept a string and calculate the number of digit and letter

s = input("Enter a string: ")

d=l=0
for count in s:
    if count.isdigit():
        d = d + 1
    elif count.isalpha():
        l = l + 1
    else:
        pass
print("digit: ", d)
print("letter: ", l)
