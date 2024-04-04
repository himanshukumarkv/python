import math
a=int(input("enter the value of a= "))
n=int(input("enter the value of n= "))
r=int(input("enter the value of r= "))
sum=0
for i in range(n+1):
    b=a*math.pow(r,i)
    print(b)
    i=i+1
    sum=sum+b
print("sum=",sum)
