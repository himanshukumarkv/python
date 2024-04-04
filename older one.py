while True:
    print("enter the age of 3 people")
    print("age of 1st person")
    a = int(input())
    print("age of 2st person")
    b = int(input())
    print("age of 3st person")
    c = int(input())
    print("age of 4st person")
    d = int(input())
    if a>b and a>c and a>d:
        print("1st is older")
    elif b>a and b>c and b>d:
        print("2nd is older")
    elif c>a and c>b and c>d:
        print("3rd is older")
    else:
        print("4 th is older")


    print("do you want to countinue [y/n]")
    ch = input()
    if ch == 'y':
        continue
    elif ch == "n":
        break
    else:
        print("please enter coreect option")
        break

