while True:
    print("enter the age of 3 people")
    print("age of 1st person")
    a = int(input())
    print("age of 2st person")
    b = int(input())
    print("age of 3st person")
    c = int(input())
    if a < b:
        if a < c:
            print("1st is yongest")
        else:
            if b > c:
                print("3ed is youngest one")
    else:
        print("2nd one is youngest")
    print("do you want to countinue [y/n]")
    a = input()
    if a == 'y':
        continue
    elif a == "n":
        break
    else:
        print("please enter coreect option")
        break

