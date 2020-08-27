# Max Digit


def max_digit(number):
    """ Returns which digit in this number is the biggest """
    return int(max(str(number)))


# Running some tests..
print(max_digit(0) == 0)
print(max_digit(52) == 5)
print(max_digit(634) == 6)
print(max_digit(1) == 1)
print(max_digit(10000) == 1)