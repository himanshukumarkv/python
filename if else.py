print("enter two number")
n1=int(input())
n2=int(input())
print("enter the choice +,-,*,/")
n3=input()
if n1==56 and n2==6 and n3=='+':
    print(72)
elif n1==45 and n2==3 and n3=='*':
    print(555)
elif n1==56 and n2==6 and n3=='/':
    print(11)
elif n3=='+':
    print(n1+n2)
elif n3=='*':
    print(n1*n2)
elif n3=='/':
    print(n1/n2)
elif n3=='-':
    print(n1-n2)
else:
    print("invailid")

