import sys

def day_01(captcha):
    return sum(int(c) for i, c in enumerate(captcha) if c == captcha[i-1])

if __name__ == '__main__':
    print(day_01(sys.argv[1]))
