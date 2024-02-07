from math import gcd, sqrt, floor


def swap(a, b):
    t = a
    a = b
    b = t
    return a, b


def gcdEuclidean(a, b):
    if b > a:
        a, b = swap(a, b)
    qs = []
    while b > 0:
        q = a // b
        r = a % b
        a = b
        b = r
        qs.append(q)

    return a, qs


def extendedEuclideanAlgorithm(a, b):
    print("Extended Euclidean Algorithm")
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    while a and b:
        q = a // b
        a, b = b, a % b
        s1, s2 = s2, s1 - q * s2
        t1, t2 = t2, t1 - q * t2
        print(f"q={q}; a={a}; b={b}; s1={s1}; s2={s2}; t1={t1}; t2={t2}")
    return s1, t1, a


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def valueFunctionEuler(n):
    if is_prime(n):
        return n - 1
    div = n - 1
    divs = []
    num = n
    while div > 1 or num > 1:
        if not is_prime(div) or num % div != 0:
            div -= 1
            continue
        num = num / div
        divs.append(div)

    euler = 1
    divs = list(set(divs))
    for div in divs:
        euler *= (1 - (1 / div))
    return floor(euler * n)
