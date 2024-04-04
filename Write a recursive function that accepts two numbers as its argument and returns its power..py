def power(x, n):
    if (n == 1):
        return x
    else:
        return x * power(x, n - 1)


# calling the power function
base = 8
exp = 3
print(base, "raised to", exp, "is", power(base, exp))