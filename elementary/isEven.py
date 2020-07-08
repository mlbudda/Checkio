# %%
# Is Even
def is_even(num):
    if (num % 2) == 0:
        return True
    else:
        return False

# Running some tests..
print(is_even(2) == True)
print(is_even(5) == False)
print(is_even(0) == True)