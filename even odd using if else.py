while True:
    print("enter a number")
    n = int(input())
    if n%2==0 or n==0:
        print("even")
    else:
        print("odd")
    print("do you want to countinue [y/n]")
    a=input()
    while a.lower() not in ("y", "n"):
        a=input("please use correct option [y/n]")
    if a=="n":
        break