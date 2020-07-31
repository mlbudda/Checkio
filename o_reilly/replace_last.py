# Replace Last

from typing import Iterable


def replace_last(items: list) -> Iterable:
    """ Last element becomes the first one """
    if len(items) > 0:
        items.insert(0, items[-1])
        items.pop(-1)
    return items


# Running some tests..
print(list(replace_last([2, 3, 4, 1])) == [1, 2, 3, 4])
print(list(replace_last([1])) == [1])
print(list(replace_last([])) == [])
