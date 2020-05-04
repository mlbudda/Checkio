#%%
# Acceptable Password I
def is_acceptable_password(password):
    return len(password) > 6

# Running some tests...
print(is_acceptable_password('short') == False)
print(is_acceptable_password('muchlonger') == True)
print(is_acceptable_password('ashort') == False)