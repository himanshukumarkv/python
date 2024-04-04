n = 50
i = 0
print("******welcome to the guessing game******")
print("==== RULE--you have 9 change to guess the number === ")
while (i<=9):
    i = i + 1
    a = int(input("enter the number b/w 0 to 100"))
    if i==9:
        print("you lost BECAUSE OF EXHAUSTED OF NUMBER OF CHANCE")
        break
    elif a > n:
        print("guessing number is too high please enter lower number ")
        continue
    elif a < n:
        print("guessing number is too lower please enter higher number ")
        continue
    else:
        print(f"you won, your number of try is {i}")
        break

