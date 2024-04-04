def getdate():
    import datetime
    return datetime.datetime.now()
def log(b):
    if b==1:
        c=int(input("enter 1 for food 2 for exercise"))
        if c==1:
            f=open("Himanshu-food.py", "a")
            f.write(str(getdate()))
            f.write(input("enter the name of food\n"))
            f.close()
        elif c==2:
            f = open("Himanshu-ex.py", "a")
            f.write(str(getdate()))
            f.write(input("  enter the name of exercise"))
            f.close()
    elif b == 2:
        c = int(input("enter 1 for food 2 for exercise"))
        if c == 1:
            f = open("Piyush-food.py", "a")
            f.write(str(getdate()))
            f.write(input("  enter the name of food"))
            f.close()
        elif c == 2:
            f = open("Piyush-ex.py", "a")
            f.write(str(getdate()))
            f.write(input("  enter the name of exercise"))
            f.close()
    elif b == 3:
        c = int(input("enter 1 for food 2 for exercise"))
        if c == 1:
            f = open("Raj-food.py", "a")
            f.write(str(getdate()))
            f.write(input("  enter the name of food"))
            f.close()
        elif c == 2:
            f = open("Raj-ex.py", "a")
            f.write(str(getdate()))
            f.write(input("  enter the name of exercise"))
            f.close()
def retrive(b):
    if b==1:
        c=int(input("enter 1 for food and 2 for exercise"))
        if c==1:
            f=open("Himanshu-food.py")
            print(f.read())
            f.close()
        elif c==2:
            f=open("Himanshu-ex.py")
            print(f.read())
            f.close()
    elif b==2:
        c = int(input("enter 1 for food and 2 for exercise"))
        if c == 1:
            f = open("Piyush-food.py")
            print(f.read())
            f.close()
        elif c == 2:
            f = open("Piyush-ex.py")
            print(f.read())
            f.close()
    elif b==3:
        c = int(input("enter 1 for food and 2 for exercise"))
        if c == 1:
            f = open("Raj-food.py")
            print(f.read())
            f.close()
        elif c == 2:
            f = open("Raj-ex.py")
            print(f.read())
            f.close()
print("******* HEATH MANAGMENT SYSTEM ******* ")
b = int(input("enter 1 for Himanshu 2 for Piyush 3 for Raj"))
if b==1:
    r=int(input("enter 1 for log 2 for retrive"))
    if r==1:
        log(1)
    elif r==2:
        retrive(1)
elif b==2:
    r=int(input("enter 1 for log 2 for retrive"))
    if r==1:
        log(2)
    elif r==2:
        retrive(2)
elif b==3:
    r=int(input("enter 1 for log 2 for retrive"))
    if r==1:
        log(3)
    elif r==2:
        retrive(3)

