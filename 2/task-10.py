# does my number look big in this
def narcissistic(value):
    number = str(value)
    number_count = len(number)
    compare = 0
    for x in number:
        compare += int(x) ** int(number_count)
    return value == compare
