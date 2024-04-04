def gre_number(a,b,c):
    if a>b and a>c:
        print(f'{a} is greater')
    elif b>a and b>c:
        print(f'{b} is greater')
    else:
        print(f'{c} is greater')
n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
n3=int(input("enter the third number"))
gre_number(n1,n2,n3)