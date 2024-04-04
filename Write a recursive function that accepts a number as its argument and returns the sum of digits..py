def sumDigits(n):
    if (n < 10):
        return n
    else:
        return n % 10 + sumDigits(n // 10)

#calling the function
number = 56
print('Sum of digits of number',number,'is',sumDigits(number))