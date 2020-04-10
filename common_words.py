# Common Words


def checkio(line1: str, line2: str) -> str:
    """ Finda what is common between these strings """
    result = []
    for i in line1.split(','):
        for j in line2.split(','):
            if i == j:
                result.append(i)
    result.sort()
    final_result = ''
    for i in result:
        final_result += i + ','
    return final_result[:-1]


# Running some tests..
print(checkio('hello,world', 'hello,earth') == 'hello')
print(checkio('one,two,three', 'four,five,six') == '')
print(checkio('one,two,three', 'four,five,one,two,six,three') == 'one,three,two')
