string = str(input())
letter = ''
frequency = 0
for x in string:
    if string.count(x) > frequency:
        frequency = string.count(x)
        letter = x
    else:
        continue
if frequency == 1:
    print('All symbols are unique')
else:
    print(letter)
