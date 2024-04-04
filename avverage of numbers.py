print("enter the number")
sum=0
ave=0
i=0
while(True):
    num=int(input())
    if num==0:
        break
    else:
        sum=sum+num
    i=i+1
ave=sum/i
print(sum)
print(ave)
