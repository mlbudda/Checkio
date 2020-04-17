# Split Pairs
def split_pairs(a):
    if (len(a) % 2) != 0:
        a += '_'
    return [a[i:i + 2] for i in range(0, len(a), 2)]

# Running some tests...
print(list(split_pairs('abcd')) == ['ab', 'cd'])
print(list(split_pairs('abc')) == ['ab', 'c_'])
print(list(split_pairs('abcdf')) == ['ab', 'cd', 'f_'])
print(list(split_pairs('a')) == ['a_'])
print(list(split_pairs('')) == [])