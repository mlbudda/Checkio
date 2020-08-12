# Remove All Before
def remove_all_before(items,border):
    try:
        return items[items.index(border):]
    except ValueError:
        return items

# Running some tests.
print(list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5])
print(list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3])
print(list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4])
print(list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7])
print(list(remove_all_before([], 0)) == [])
print(list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7])