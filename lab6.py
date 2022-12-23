
def Evklid_NOD_div(a: int, b: int):
    while a != 0 and b != 0:
        if a > b:
            print(a, " % ", b, " = ", a % b)
            a = a % b
        else:
            print(b, " % ", a, " = ", b % a)
            b = b % a
    return a + b


def Evklid_NOD_min(a: int, b: int):
    while a != b:

        if a > b:
            print(a, " - ", b, " = ", a - b)
            a = a - b
        else:
            print(b, " - ", a, " = ", b - a)
            b = b - a
            
    return a


def bezout_recursive(a, b):

    if not b:
        return (1, 0, a)
    y, x, g = bezout_recursive(b, a % b)
    return (x, y - (a // b) * x, g)

    


def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans


def task4(a):
    for i in range(1, 101):
        
        print((2 ** i) % a)


if __name__ == '__main__':
    #assert Evklid_NOD_min(72, 26) == 2
    #assert Evklid_NOD_div(72, 26) == 2

    print(bezout_recursive(5999801, 48685811))
    #print(Evklid_NOD_min(5999801, 48685811))
    #print(Factor(5999801))
    #print(Factor(48685811))
    task4(17)
