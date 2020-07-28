# Date and Time Converter
import datetime

def date_time(time):
    d = datetime.date(int(time[6:10]), int(time[3:5]), int(time[0:2], ))
    t = datetime.time(int(time[11:13]), int(time[14:16]))
    hours_str = 'hours'
    minutes_str = 'minutes'
    if int(time[11:13]) == 1:
        hours_str = 'hour'
    if int(time[-2:]) == 1:
        minutes_str = 'minute'
    result = '{0:%-d} {0:%B} {0:%Y} year {1:%-H} {2} {1:%-M} {3}'.format(d, t, hours_str, minutes_str)
    return result


print(date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium")
print(date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory")
print(date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born")
