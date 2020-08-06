# Beginning Zeros
def beginning_zeros(number):
    # your code here
    counter = 0
    for i in number:
        if i == '0':
            counter += 1
        elif i != '0':
            break
    return counter

# Running some tests..
print(beginning_zeros('100') == 0)
print(beginning_zeros('001') == 2)
print(beginning_zeros('100100') == 0)
print(beginning_zeros('001001') == 2)
print(beginning_zeros('012345679') == 1)
print(beginning_zeros('0000') == 4)