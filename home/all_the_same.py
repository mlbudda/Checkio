# All the Same

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    """  Checks if all elements in the given list are equal """
    result = True
    for i in elements:
        if elements.count(i) != len(elements):
            result = False
    return result


# Running some tests..
print(all_the_same([1, 1, 1]) == True)
print(all_the_same([1, 2, 1]) == False)
print(all_the_same(['a', 'a', 'a']) == True)
print(all_the_same([]) == True)
print(all_the_same([1]) == True)