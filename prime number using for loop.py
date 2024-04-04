print("enter number")
a = int(input())
f=0
if a==0 or a==1:
    f=1
for i in range(2, a):
    if a % i==0:
        f=1
if f==1:
    print("not prime")
else:
    print("prime")

