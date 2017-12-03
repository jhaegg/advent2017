import sys

def day_01(captcha, offset):
    return sum(int(c) for i, c in enumerate(captcha) if c == captcha[(i + offset) % len(captcha)])

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(day_01(sys.argv[1], len(sys.argv[1]) // 2))
    else:
        print(day_01(sys.argv[1], int(sys.argv[2])))
