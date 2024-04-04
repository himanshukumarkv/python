a = int(input("emter the number of rows"))
for i in range(1,a+1):
    for j in range(i-1):
        print("*", end=" ")
    print()
for i in range(a,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()