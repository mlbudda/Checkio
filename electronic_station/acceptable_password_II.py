# Acceptable Password II

def is_acceptable_password(password: str) -> bool:
    """ Checks for > 6 character and at least 1 digit """
    if len(password) > 6:
        contains_digit = False
        for i in password:
            if i.isdigit():
                contains_digit = True
        return contains_digit
    else:
        return False


# Running some tests..
print(is_acceptable_password('short') == False)
print(is_acceptable_password('muchlonger') == False)
print(is_acceptable_password('ashort') == False)
print(is_acceptable_password('muchlonger5') == True)
print(is_acceptable_password('sh5') == False)

