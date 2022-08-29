# RGB to hex conversion
def rgb(r, g, b):
    R = f'{r:X}'
    G = f'{g:X}'
    B = f'{b:X}'
    if r < 0:
        R = '00'
    if g < 0:
        G = '00'
    if b < 0:
        B = '00'
    if len(R) < 2:
        R = '0' + R
    if len(G) < 2:
        G = '0' + G
    if len(B) < 2:
        B = '0' + B
    if int(r) > 255:
        R = 'FF'
    if int(g) > 255:
        G = 'FF'
    if int(b) > 255:
        B = 'FF'
    return R+G+B
