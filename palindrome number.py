num=int(input("enter a number"))
a=num
rev=0
while(True):
    dig=num%10
    rev = rev * 10 + dig
    num=num//10
    if num==0:
        break
    else:
        continue
if a==rev:
    print("a palindrome number")
else:
    print("not a palindrome number")

