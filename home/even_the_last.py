# Even the Last
def checkio(array):
    result = 0
    if array:
        for i in array[::2]:
            result = i + result
        result = result*array[-1]
    return result

# Running some tests..
print(checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30")
print(checkio([1, 3, 5]) == 30, "(1+5)*5=30")
print(checkio([6]) == 36, "(6)*6=36")
print(checkio([]) == 0, "An empty array = 0")
