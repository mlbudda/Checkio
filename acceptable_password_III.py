# Acceptable Password III


def is_acceptable_password(password: str) -> bool:
    """ Check if > 6 characters and has at least one digit, 
    but not only digits """
    result = False
    if len(password) > 6 and not password.isdigit():
        for i in password:
            if i.isdigit():
                result = True
                break
    return result


# Running some tests..
print(is_acceptable_password('short') == False)
print(is_acceptable_password('muchlonger') == False)
print(is_acceptable_password('ashort') == False)
print(is_acceptable_password('muchlonger5') == True)
print(is_acceptable_password('sh5') == False)
print(is_acceptable_password('1234567') == False)
