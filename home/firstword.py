# First Word
def first_word(text):
    text_converted = str(text).lstrip(". ,")
    s = ''
    for i in text_converted:
        if i.isalpha():
            s = s + i
        elif i == "'":
            s = s + i
        else:
            break
    return s

# Running sme tests...
print(first_word("Hello world") == "Hello")
print(first_word(" a word ") == "a")
print(first_word("don't touch it") == "don't")
print(first_word("greetings, friends") == "greetings")
print(first_word("... and so on ...") == "and")
print(first_word("hi") == "hi")
print(first_word("Hello.World") == "Hello")
