# Three Words
def checkio(words: str) -> bool:
    counter = 0
    a = 0
    for i in words.split():
        if i.isalpha():
            counter += 1
        else:
            counter = 0
        if counter >= 3:
            a = 1

    if a == 0:
        return False
    else:
        return True

# Running some
print(checkio("Hello World hello") == True, "Hello")
print(checkio("He is 123 man") == False, "123 man")
print(checkio("1 2 3 4") == False, "Digits")
print(checkio("bla bla bla bla") == True, "Bla Bla")
print(checkio("Hi") == False, "Hi")
