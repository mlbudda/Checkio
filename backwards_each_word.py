# Backward Each Word

def backward_string_by_word(text: str) -> str:
    """ Reverses every word, keeps words in their original places """
    word_list = text[::-1].split()
    word_list.reverse()
    s1 = ''
    result = ''

    for word in word_list:
        s1 = s1 + word
    s1 = list(s1)

    i = 0
    for letter in text:
        if letter.isalpha():
            result = result + s1[i]
            i += 1
        else:
            result = result + ' '
    return result

# Running some tests..
print(backward_string_by_word('') == '')
print(backward_string_by_word('world') == 'dlrow')
print(backward_string_by_word('hello world') == 'olleh dlrow')
print(backward_string_by_word('hello   world') == 'olleh   dlrow')
print(backward_string_by_word('welcome to a game') == 'emoclew ot a emag')
