import math
def f (x):
    y = x**7 + 24 * x**5 + 48/(x**5/95) - 43 * (x**3) - (x**3 + 69 * x**8 - 96) - (x**6 - x**5)
    return y

print(f(-73))

def f1(x):
    if(x < 73):
        x ** 7 + 24 * x ** 5 + 48
    elif(x >= 73 & x < 152):
        y = ((abs(x) - x**3)**5)/59 - x**3/21
    elif(x >= 152):
        y = (x**6 - x**5)**4/15 + x**5

    return y

print(f1(98))

def f2(n,m):
    y = 57 * p1(n,m) + p2(n)
    return y

def p1(n,m):
    e = 2.7182818284
    y = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
           y = y + (e**j + (27 * (i**8)))
    return y

def p2(n):
    z = 0
    for i in range(1,n+1):
        z = z + ((72 * (i**2)) - i**6)
        return z

print(f2(50,64))
def f3(n):
    if(n == 0):
        return 7
    else:
        return abs(f3(n-1)) + math.tan(f3(n-1))

print(f3(7))
