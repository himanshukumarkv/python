sal=float(input("salary of a employee\n"))
bonus=0
t=float(input("time period of sevice in year\n"))
if t>10:
    bonus=(sal*10/100)
elif 6 <= t <= 10:
    bonus=(sal*8/100)
else:
    bonus = (sal * 5 / 100)
print("bonus= ", bonus)




