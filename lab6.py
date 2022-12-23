
def Evklid_NOD_div(a: int, b: int):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def Evklid_NOD_min(a: int, b: int):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


if __name__ == '__main__':
    assert Evklid_NOD_min(72, 26) == 2
    assert Evklid_NOD_div(72, 26) == 2
