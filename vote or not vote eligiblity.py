while True:
    print("enter the age")
    age=int(input())
    if age>100 or age<0:
        print("age is not proper")
    elif age>=18 and age<=100:
        print("can vote")
    elif age >=0 and age <18:
        print("can\'t vote")
    print("do you want to countinue [y/n]")
    a=input()
    while a.lower() not in ("y", "n"):
        a=input("please use correct option [y/n]")
    if a=="n":
        break







