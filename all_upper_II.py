# All Upper II

def is_all_upper(text: str) -> bool:
    """ Checks if a given string has all symbols in upper case """
    return text.isupper()

# Running some tests..
print(is_all_upper('ALL UPPER') == True)
print(is_all_upper('all lower') == False)
print(is_all_upper('mixed UPPER and lower') == False)
print(is_all_upper('') == False)