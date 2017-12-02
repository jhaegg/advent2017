def day_01(captcha):
    return sum(int(c) for i, c in enumerate(captcha) if c == captcha[i-1])
