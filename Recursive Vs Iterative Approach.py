# def fact(n):
#     f=1
#     if n==0:
#         return 1
#     for i in range(1,n+1):
#         f=f*i
#         i=i+1
#     return f
# n=int(input("enter a number"))
# print("factorial is ",fact(n))
# def fac(n):
#     if n == 0:
#         return 1
#     elif n < 0:
#         print("invalid input")
#     else:
#         return n * fac(n - 1)
#
#
# n = int(input('enter a number'))
# print("factorial is ", fac(n))
def fab(n):
        if n==1:
            f=0
            return f
        elif n==2 or n==3:
            f=1
            return f
        else:
            f=fab(n-1)+fab(n-2)
            return f
n=int(input("enter a number"))
f=fab(n)
print(fab(n))
