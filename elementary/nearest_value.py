# Nearest Value


def nearest_value(values,one):
    """ Finds the nearest value to the given one """
    values_list = list(values)
    values_list.sort()
    if values_list.count(one):
        return one
    elif one > values_list[-1]:
        return values_list[-1]
    elif one < values_list[0]:
        return values_list[0]
    else:
        values_list.append(one)
        values_list.sort()
        values_list.index(one)
        a = values_list[values_list.index(one)] - values_list[values_list.index(one) - 1]
        b = values_list[values_list.index(one) + 1] - values_list[values_list.index(one)]
        if a <= b:
            return values_list[values_list.index(one) - 1]
        else:
            return values_list[values_list.index(one) + 1]


# Running some tests...
print(nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10)
print(nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7)
print(nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8)
print(nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9)
print(nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4)
print(nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17)
print(nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8)
print(nearest_value({-1, 2, 3}, 0) == -1)