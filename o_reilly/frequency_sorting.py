# Frequency Sorting


def frequency_sorting(numbers):
    """ Sorts the list by the frequency of numbers included in it """
    numbers.sort()
    return sorted(numbers, key=lambda x: numbers.count(x), reverse=True)


# Running some tests..
print(frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted")
print(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [4, 4, 4, 3, 3, 11, 11, 7, 13], "Not sorted")
print(frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [10, 10, 21, 21, 55, 55, 99, 99], "Reversed")
