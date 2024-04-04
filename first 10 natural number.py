while(True):
    print("enter the digit you want to product them")
    a=int(input())
    p=1
    for i in range(1,a+1):
        b=int(input(f"{i} number"))
        p=p*b
    print(p)
    print("do you want to countinue [y/n]")
    c=input()
    while a.lower() not in ("y", "n"):
        a = input("please use correct option [y/n]")
    if a == "n":
        break






