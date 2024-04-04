print("enter a number")
n = int(input())
a = n%10
print("last digit=", a)
if a%3==0:
    print("divisble by 3 and the last digit is ", a)
else:
    print("not divigible by 3")
