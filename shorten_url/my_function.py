def check_email(email):
    if len(email) == 0 or '@' not in email or '.' not in email:
        return False
    return True
    
def check_value(a, b, c):
    if a + b == c:
        return True
    return False