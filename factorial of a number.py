while(True):
    print("enter a number")
    a = int(input())
    f = 1
    for i in range(1, a + 1):
       f = f * i
       i = i - 1
    print(f"factorial of {a} =", f)
    print("do you want to countinueo [y/n]")
    a = input()
    while a.lower() not in ('y','n'):
        a=input("y/n")
    if a == 'n':
        break

