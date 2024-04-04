n=int(input("enter anmber"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("not a prime")
        else:
            print("prime number")
        break
else:
    print("not a prime number")
