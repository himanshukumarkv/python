def decToBinary(num):
    if (num == 0):
        return

    decToBinary(num // 2)
    print(num % 2,end="")


#calling the function
number = 45
print("Decimal equivalent of",number,"is ",end="")
decToBinary(number)