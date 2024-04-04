# n=int(input("nmber"))
# n1=int(input("nmber1"))
# if n>n1:
#     min=n1
# else:
#     min=n
# for i in range(1,min+1):
#     if n%i==0 and n1%i==0:
#         gcd=i
# print("gcd=",i)
def gcd(num1,num2):
    if num2!=0:
        return gcd(num2,num1%num2)
    else:
        return num1


num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
if num1>num2:
    min=num2
    max=num1
else:
    min=num1
    max=num2
hcf=gcd(max,min)
print("gcd=",hcf)
