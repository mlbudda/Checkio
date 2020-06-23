# Surjection Strings

def isometric_strings(str1: str, str2: str) -> bool:
    """ Checks that the 2 given strings are isometric """
    result = False
    if str1 == str2:
        result = True
    else:
        for i in range(len(str1)):
            if (str1.count(str1[i])) != (str2.count(str2[i])):
                result = False
                break
            else:
                result = True
    return result


# Running some tests...
print(isometric_strings('add', 'egg') == True)
print(isometric_strings('foo', 'bar') == False)
print(isometric_strings('', '') == True)
print(isometric_strings('all', 'all') == True)