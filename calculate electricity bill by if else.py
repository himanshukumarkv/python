#     unit                       bill
# first 100 unit               no charge
# after 100 unit             rs 5/unit
# after 200 unit               rs 10/unit
#    input total bill 2000 for 350 unit
print("enter the unit")
unit = float(input())
if unit < 100:
    bill = 0
elif 100 <= unit < 200:
    bill = (unit-100)*5
else:
    bill = 500+ (unit-200)*10
print("bill=", bill)



