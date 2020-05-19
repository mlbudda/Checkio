# Bigger Price
def bigger_price(limit: int, data: list) -> list:
    a = []
    for j in data:
        a.append(j['price'])
    a.sort()
    result = []
    i = 0
    while i != limit:
        for j in data:
            if j['price'] == a[(-1) - i]:
                result.append(j)
        i += 1
    return result

# Running some tests...
print(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
               {"name": "wine", "price": 138},
               {"name": "bread", "price": 100}
           ], "First")

print(bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second")

