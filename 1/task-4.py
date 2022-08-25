decode = str(input())
red, green, blue = decode[0:2], decode[2:4], decode[4:6]
print('Red: ', int(red, 16), '\n', 'Green: ', int(green, 16), '\n', 'Blue: ', int(blue, 16), sep='')