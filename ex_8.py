def is_palindrome(pal):
    nova = ''
    for i in pal:
        nova  = i + nova
    if nova == pal:
        return True
    return False