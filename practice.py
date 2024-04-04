# l=["aaple","orange","poji","rekh", "a"]
# a=[]
# print(l)
# for i in l:
#     if "a" in i:
#         a.append(i)
# print(a)
# l=[]
# a=int(input("enter the number of element"))
# for i in range(1,a+1):
#     n=int(input(f"{i} element"))
#     l.append(n)
# print(l)
# b=int(input("enter the number you want to search"))
# if b in l:
#     print("p")
# else:
#     print("n")
# f=open("ram.py","w")
# f.write("himanshu is a good boy")
# f.write("himjkuuyhh")
# f.close()
# f=open("ram.py","r")
# print(f.read())
# f.close()
# f=open("ram.py","a")
# f.write("lkjhggg")
# f.close()
# f=open("ram.py")
#
# print(f.read())
# n=int(input("enter a number"))
# cop=n
# sum=0
# b=len(str(n))
# print(b)
# while(n>0):
#     if n==0:
#         break
#     else:
#         a=n%10
#         sum=sum+pow(a,b)
#         n=n//10
# print(sum)
# if sum==cop:
#     print("u")
# else:
#     print("n")
n=int(input("enter a number"))
b=n
sum=0
while(True):
    f = 1
    a=n%10
    for i in range(1,a+1):
        f=f*i
        i=i+1
    print(f)
    sum=sum+f
    n=n//10
    if n==0:
        break
    else:
        continue
print(sum)
if sum==b:
    print("y")
else:
    print("n")







