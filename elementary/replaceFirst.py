# Replace First
def replace_first(items):
    if len(items) >= 1:
        items.append(items[0])
        x = items[0]
        items.remove(x)
    return items

# Running some test
print(list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1])
print(list(replace_first([1])) == [1])
print(list(replace_first([])) == [])