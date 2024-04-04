while True:
    print("enter the marked price")
    mp=float(input())
    if mp>10000:
        ds=mp*20/100
    elif mp>7000 and mp<=10000:
        ds=mp*15/100
    elif mp<=7000:
        ds=mp*10/100
    na=mp-ds
    print("Net ammount= ", na)
    print("do you want countinue[y/n]")
    a=input()
    while a.lower() not in ("y","n"):
        a=input("please use correct option [y/n]")
    if a=="n":
        break