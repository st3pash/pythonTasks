amount = int(input()) // 10
if amount > 10 or amount < 0:
    print('Некорректное значение громкости!')
else:
    print('|', end='')
    for amount in range(amount):
        print('>', end='')
    if amount < 10:
        print(' ' * (9 - amount), end='')
    print('|')