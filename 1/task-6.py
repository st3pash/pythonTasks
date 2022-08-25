m, n = int(input()), int(input())
o = m
mono = ' *'
multi = list(mono * (m * n // 2))
while n > 0:
    multi.insert(m, '\n')
    m += o + 1
    n -= 1
print(*multi, sep='')