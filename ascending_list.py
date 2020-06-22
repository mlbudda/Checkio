# Ascending List

from typing import Iterable


def is_ascending(items: Iterable[int]) -> bool:
    """ Determine whether the sequence of elements items is ascending """
    help_list = sorted(items)
    make_list = list(items)
    counter = False
    for i in make_list:
        if make_list.count(i) > 1:
            counter = True
    if counter:
        return False
    elif items == help_list:
        return True
    else:
        return False


# Running some tests..
print(is_ascending([-5, 10, 99, 123456]) == True)
print(is_ascending([99]) == True)
print(is_ascending([4, 5, 6, 7, 3, 7, 9]) == False)
print(is_ascending([]) == True)
print(is_ascending([1, 1, 1, 1]) == False)
