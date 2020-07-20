# Goes Right After

def goes_after(word: str, first: str, second: str) -> bool:
    """ Checks if one symbol goes right after another """
    try:
        return (word.index(second) - word.index(first)) == 1
    except ValueError:
        return False


# Running some tests..
print(goes_after('world', 'w', 'o') == True)
print(goes_after('world', 'w', 'r') == False)
print(goes_after('world', 'l', 'o') == False)
print(goes_after('panorama', 'a', 'n') == True)
print(goes_after('list', 'l', 'o') == False)
print(goes_after('', 'l', 'o') == False)
print(goes_after('list', 'l', 'l') == False)
print(goes_after('world', 'd', 'w') == False)
