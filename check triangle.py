while True:
    print("enter the sides of triangle")
    a=int(input("1 side"))
    b = int(input("2 side"))
    c = int(input("3 side"))
    if a==b==c:
        print("equilateral")
    elif (a==b) or (b==c) or (c==a):
        print("isosceles")
    else:
        print("scalene")
    print("couninue[y/n]")
    z=input()
    while z.lower() not in ("y","n"):
        z=input("enter correct option[y/n]")
    if z=="n":
        break


