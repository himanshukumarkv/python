n= int(input("enter the number of rows"))
for i in range(n-1):
    for j in range(i,n):
        print("* ", end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print("* ", end=" ")
    print()