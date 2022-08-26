string = input()
v = int(input())
y = 'abcdefghijklmnopqrstuvwxyz{} ~'
for x in string:
    index_y = y.index(x)
    index_x = string.index(x)
    u = string.replace(x, y[index_y + v])
    print(u[index_x], end='')