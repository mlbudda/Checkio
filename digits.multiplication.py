# Digits Multiplication

def checkio(number: int) -> int:
    """ Calculates the product of the digits excluding any zeroes """
    total = 1
    for i in str(number):
        if i != '0':
            total = total * int(i)
    return total


# Running some tests..
print(checkio(123405) == 120)
print(checkio(999) == 729)
print(checkio(1000) == 1)
print(checkio(1111) == 1)
