

# write a program to print th grade of the student 
# conditions---> 91-100=A+ |  71-80=B+  | 41-70=C+ | less tahn or equal to 40 == fail

a = int(input("Enter the pecntage of studennt: "))
# int(a)

if a>=91 and a<=100 :
    print("Grade:A+")
elif a>=71 and a<=90:
    print("Grade:B+")
elif a>=41 and a<=70:
    print("Grade:C+")
else :
    print("Fail")


