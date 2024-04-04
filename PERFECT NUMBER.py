n=int(input("enter a number"))
sum=0
for i in range(1,n):
    if n%i==0:
        print(i)
        sum=sum+i
        i=i+1
if n==sum:
    print("perfect number")
else:
    print("non perpect")
