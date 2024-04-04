# a = 10  # global variable


# def man():
#     # a = 5  # local variable
#     m = 66  # local
#     global a #global keyword
#     a=a+45
#     print(a, m)
#
#
# man()
# print(a)

x = 80
def harry():
    x = 20
    def rohan():
        global x
        x = 88
    # print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)

harry()
print(x)