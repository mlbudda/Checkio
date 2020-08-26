#%%
# Correct Sentence


def correct_sentence(text):
    """ Returns a corrected version, that starts 
    with a capital letter and ends with a period (dot) """
    if text[0].islower():
        text = text.replace(text[0], text[0].swapcase(), 1)
    if not text.endswith('.'):
        text += '.'
    return text


# Running some test...
print(correct_sentence("greetings, friends") == "Greetings, friends.")
print(correct_sentence("Greetings, friends") == "Greetings, friends.")
print(correct_sentence("Greetings, friends.") == "Greetings, friends.")
print(correct_sentence("hi") == "Hi.")
print(correct_sentence("welcome to New York") == "Welcome to New York.")
