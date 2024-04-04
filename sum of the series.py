x=int(input("enter the value of x "))
n=int(input("enter the value of n"))
total=0
for i in range(n+1):
    if i==0 or i==1:
        fact=1
    else:
        fact=fact*i
    sum=pow(x,i)/fact
    print(sum)
    total=total+sum
    i = i + 1
print(total)




import math
n=int(input("n="))
x=int(input("x="))
s=1.0
for i in range(1,n+1):
    s=s+math.pow(x,i)/math.factorial(i)
print(s)