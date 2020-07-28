# Sum Numbers

def sum_numbers(text: str) -> int:
    """ Sums the numbers only """
    result = 0
    for i in text.split():
        if i.isdigit():
            result = result + int(i)
    return result


# Running some tests.. 
print(sum_numbers('hi') == 0)
print(sum_numbers('who is 1st here') == 0)
print(sum_numbers('my numbers is 2') == 2)
print(sum_numbers('This picture is an oil on canvas '
                       'painting by Danish artist Anna '
                       'Petersen between 1845 and 1910 year') == 3755)
print(sum_numbers('5 plus 6 is') == 11)
print(sum_numbers('') == 0)