# End Zeros


def end_zeros(num):
    """ Finds out how many zeros a given number has at the end """
    result = 0
    for i in str(num)[::-1]:
        if int(i) == 0:
            result = result + 1
        else:
            break
    return result


# Running some tests..
print(end_zeros(0) == 1)
print(end_zeros(1) == 0)
print(end_zeros(10) == 1)
print(end_zeros(101) == 0)
print(end_zeros(245) == 0)
print(end_zeros(100100) == 2)