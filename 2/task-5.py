# detect pangram
def is_pangram(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    for letter in alphabet:
        if letter in s:
            continue
        else:
            return False
    return True