# Second Index
def second_index(text,symbol):
    res = [i for i in range(len(text)) if text.startswith(symbol, i)]
    if len(res) >= 2:
        return res[1]
    else:
        return None

# Running some tests..
print(second_index("sims", "s") == 3, "First")
print(second_index("find the river", "e") == 12, "Second")
print(second_index("hi", " ") is None, "Third")
print(second_index("hi mayor", " ") is None, "Fourth")
print(second_index("hi mr Mayor", " ") == 5, "Fifth")