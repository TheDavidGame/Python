import math


def f11(x):
    return (((x ** 7) + (24 * (x ** 5)) + 48) / ((x ** 5) / 95) - (43 * (x ** 3))) - ((x ** 3) + (69 * (x ** 8)) - 96) - x


print(f11(-73))
def f12(x):
    if x < 73:
        return (x ** 7) + (24 * (x ** 5)) + 48
    elif 73 <= x < 152:
        return ((abs(x) - x ** 3) ** 5) / 59 - x ** 3 / 21
    elif x >= 152:
        return ((x ** 6 - x ** 5) ** 4)/ 15 + x ** 5


def f13(n, m):
    return 57 * p1(n, m) + p2(n)


def p1(n, m):
    e = 2.7182818284
    y = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            y = y + (e ** j + (27 * (i ** 8)))
    return y


def p2(n):
    z = 0
    for i in range(1, n + 1):
        z = z + ((72 * (i ** 2)) - i ** 6)
        return z


def f14(n):
    if n == 0:
        return 7
    else:
        return abs(f14(n - 1)) + math.tan(f14(n - 1))