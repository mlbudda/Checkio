# Non-unique Elements
def checkio(data: list) -> list:
    numbers_remove = []

    for number in data:
        if data.count(number) == 1:
            numbers_remove.append(number)
    for number in numbers_remove:
        data.remove(number)
    return data

# Running some tests...
print(list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example")
print(list(checkio([1, 2, 3, 4, 5])) == [], "2nd example")
print(list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example")
print(list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example")
