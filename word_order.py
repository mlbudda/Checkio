# Words Order

def words_order(text: str, words: list) -> bool:
    """ Checks if the words in a list appear in the same 
        order as in the given text """
    custom = []
    for i in text.split():
        if i in words:
            custom.append(i)
    if words.count(words[0])>=2:
        return False
    elif words == custom:
        return True
    else:
        return False


# Running some tests..
print(words_order('hi world im here', ['world', 'here']) == True)
print(words_order('hi world im here', ['here', 'world']) == False)
print(words_order('hi world im here', ['world']) == True)
print(words_order('hi world im here',
                       ['world', 'here', 'hi']) == False)
print(words_order('hi world im here',
                       ['world', 'im', 'here']) == True)
print(words_order('hi world im here',
                       ['world', 'hi', 'here']) == False)
print(words_order('hi world im here', ['world', 'world']) == False)
print(words_order('hi world im here',
                       ['country', 'world']) == False)
print(words_order('hi world im here', ['wo', 'rld']) == False)
print(words_order('', ['world', 'here']) == False)