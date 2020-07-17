# Time Converter (24h to 12h)


def time_converter(time):
    """ Converts from 24h to 12h format """
    if int(time[:2]) > 12:
        hour = int(time[:2])-12
        result = str(hour) + time[2:] + ' p.m.'
    elif int(time[:2]) == 12:
        hour = int(time[:2])
        result = str(hour) + time[2:] + ' p.m.'
    elif int(time[1]) == 0:
        result = str(int(time[1:2])+12) + time[2:] + ' a.m.'
    else:
        result = time[1:2] + time[2:] + ' a.m.'
    return result


# Running some tests..
print(time_converter('09:00') == '9:00 a.m.')
print(time_converter('23:15') == '11:15 p.m.')
