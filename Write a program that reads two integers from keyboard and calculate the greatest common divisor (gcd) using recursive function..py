def gcd(x, y):
    if (x % y == 0):
        return y
    else:
        return gcd(y, x % y)


#calling the gcd function
num1 =int(input("n1="))
num2 =int(input("n2="))
print(num1,"and",num2,"gcd is", gcd(num1,num2))

