# multiples of 3 or 5
def solution(number):
    finish = 0
    number -= 1
    for x in range(number):
        if number < 0:
            return 0
        else:
            if number % 5 == 0 or number % 3 == 0:
                finish += number
                number -= 1
            else:
                number -= 1
    return finish