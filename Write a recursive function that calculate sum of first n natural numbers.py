def sum(n):
    if (n == 0):
        return 0
    else:
        return n + sum(n - 1)


# calling the function
number = 10
print("The sum of first", number, "number is", sum(number))