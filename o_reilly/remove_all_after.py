# Remove all after

from typing import Iterable


def remove_all_after(items: list, border: int) -> Iterable:
    """ Removes all of the elements after the given one from list """
    try:
        return items[:(items.index(border)+1)]
    except ValueError:
        return items


# Running some tests...
print(list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3])
print(list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2])
print(list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) == [1, 1, 2])
print(list(remove_all_after([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7])
print(list(remove_all_after([], 0)) == [])
print(list(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7])
