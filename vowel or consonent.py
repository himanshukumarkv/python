print("enter the alphabet")
alpha=input()
vow="aeiouAEIOU"
if alpha in vow:
    print("vowel")
else:
    if alpha.isnumeric():
        print("wrong input")
    else:
        print("not vowel")