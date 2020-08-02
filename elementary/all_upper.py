# All Upper
def is_all_upper(text):
    return text.upper() == text

# Running some tests..
print(is_all_upper('ALL UPPER') == True)
print(is_all_upper('all lower') == False)
print(is_all_upper('mixed UPPER and lower') == False)
print(is_all_upper('') == True)