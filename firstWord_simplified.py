# First Word (simplified)
def first_word(text):
    return text.rsplit()[0]

# Running some tests...
print(first_word("Hello world") == "Hello")
print(first_word("a word") == "a")
print(first_word("hi") == "hi")