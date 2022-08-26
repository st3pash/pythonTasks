# a square of squares
def is_square(n):
    if n < 0:
        return False
    a = n ** 0.5
    if a.is_integer() == True:
        return True
    else:
        return False
