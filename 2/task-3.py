# return masked string
def maskify(cc):
    if len(cc) <= 4:
        return cc
    else:
        a = cc[-1:-5:-1]
        b = cc[:-4]
        c = '#' * len(b)
        d = c + a[::-1]
        return d