


# def con_vol(name):
#     con = 0
#     vol = 0
#     el=0
#     for i in name:
#         if i in "aieou":
#             vol=vol+1
#         elif i in " ":
#             el=el+1
#         else:
#             con=con+1
#     print("vowel= ", vol)
#     print("consonent= ", con)
#     print("space=",el)
# x=input("enter the a word")
# con_vol(x)
# l=[8,47,76,34,9]
# n=len(l)
# for i in range(n):
#     min_index=i
#     for j in range(i+1,n):
#         if l[j]<l[min_index]:
#             min_index=j
#         l[j],l[min_index]=l[min_index],l[j]
# print(l)
l=[5,6,45,78]
for i in l:
    if i%2==0:
        print(f"{i}")
    else:
        print("mmm")

