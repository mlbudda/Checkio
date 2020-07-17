# Absolute Sorting

def checkio(numbers_array: tuple) -> list:
    return sorted(numbers_array, key=abs)


# Running some tests..
print(checkio((-20, -5, 10, 15)) == [-5, 10, 15, -20], "Example")  # or (-5, 10, 15, -20)
print(checkio((1, 2, 3, 0)) == [0, 1, 2, 3], "Positive numbers")
print(checkio((-1, -2, -3, 0)) == [0, -1, -2, -3], "Negative numbers")
