# build a pile of cubes
def find_nb(M):
    m = 0
    n = 0
    while m < M:
        m += n ** 3
        if m == M:
            return n
        n += 1
    return -1