# first non-repeating character
def first_non_repeating_letter(string):
    string = string.lower()
    if  len(string) == 0:
        return ''
    else:
        for i in string:
            x = string.count(i)
            if x == 1:
                return string[string.index(i)]