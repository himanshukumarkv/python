a=int(input("total number of working days\n"))
b=int(input("total number of days of absent\n"))
c=((a-b)/a)*100
print(c)
if c>=75:
    print("student will be able to sit in exam")
else:
    print("student will not be able to sit in exam")