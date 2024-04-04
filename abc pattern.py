n=5
p=65
for i in range(n):
    for i in range(i+1):
        print(chr(p),end=" ")
        p=p+1
    print()