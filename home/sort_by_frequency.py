# Sort Array by Element Frequency
def frequency_sort(items):
    """ Sorts elements by decreasing frequency order """
    return sorted(items, key=lambda x: (-items.count(x), items.index(x)))


# Running some tests..
print(list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2])
print(list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex'])
print(list(frequency_sort([17, 99, 42])) == [17, 99, 42])
print(list(frequency_sort([])) == [])
print(list(frequency_sort([1])) == [1])