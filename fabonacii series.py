def febonacii(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return febonacii(n-1)+febonacii(n-2)
n=int(input("enter the number"))
print(febonacii(n))