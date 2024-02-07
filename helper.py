from math import gcd, sqrt, floor


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
        # print(euler)
    return floor(euler * n)
