# Split List

def split_list(items: list) -> list:
    """ Splits a given array into two arrays """
    result = []
    calc = int(len(items) / 2)
    if (len(items) % 2) == 0:
        result.append(items[:calc])
        result.append(items[calc:])
    else:
        result.append(items[:calc + 1])
        result.append(items[calc + 1:])
    return result


# Running some tests..
print(split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]])
print(split_list([1, 2, 3]) == [[1, 2], [3]])
print(split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]])
print(split_list([1]) == [[1], []])
print(split_list([]) == [[], []])