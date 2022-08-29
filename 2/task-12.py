# bouncing balls
def bouncing_ball(h, bounce, window):
    if h > 0 and 0 < bounce < 1 and window < h:
        res = 0
        while h > window:
            res += 1
            h *= bounce
            if h > window:
                res += 1
        return res
    else:
        return -1