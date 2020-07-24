# Days Between
from datetime import date

def days_diff(a, b):
    x = str(a)[1:-1].split(',')
    a = date(int(x[0]), int(x[1]), int(x[2]))
    y = str(b)[1:-1].split(',')
    b = date(int(y[0]), int(y[1]), int(y[2]))
    return abs((a - b).days)

# Running some tests..
print(days_diff((1982, 4, 19), (1982, 4, 22)) == 3)
print(days_diff((2014, 1, 1), (2014, 8, 27)) == 238)
print(days_diff((2014, 8, 27), (2014, 1, 1)) == 238)
