# Popular Words
def popular_words(text, words):
    text = text.lower()
    dict = {}

    for word in words:
        dict.update({word: 0})
    for i in text.split():
        for j in words:
            if i == j:
                dict[i] += 1
    return dict

# Running some tests..
print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    })