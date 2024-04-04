num1 = int(input("1 number"))
num2 = int(input("2 number"))
f=0
for i in range(num1,num2):
    if i==0 or i==1:
        print(f"{i} is not a prime number")
    elif i==2 or i==3:
        print(f"{i} is prime number")
    elif i%2==0 or i%3==0:
            print(f"{i} is not a prime number")
    else:
        print(f"{i} is a prime number")


