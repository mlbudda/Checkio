# Sum by Type

from typing import Tuple

def sum_by_types(items: list) -> Tuple[str, int]:
    """ Returns concatenated string or sum of numbers """
    numbers = 0
    text = ''
    for i in items:
        if type(i) == int:
            numbers += i
        else:
            text += i
    return text, numbers


# Running some tests..
print(sum_by_types([]) == ('', 0))
print(sum_by_types([1, 2, 3]) == ('', 6))
print(sum_by_types(['1', 2, 3]) == ('1', 5))
print(sum_by_types(['1', '2', 3]) == ('12', 3))
print(sum_by_types(['1', '2', '3']) == ('123', 0))
print(sum_by_types(['size', 12, 'in', 45, 0]) == ('sizein', 57))
