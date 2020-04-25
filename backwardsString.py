# Backward String
def backward_string(val: str) -> str:
    return val[::-1]

# Running some tests..
print(backward_string('val') == 'lav')
print(backward_string('') == '')
print(backward_string('ohho') == 'ohho')
print(backward_string('123456789') == '987654321')