from math import sqrt, floor
from helper import swap


class MyMath:

    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def valueFunctionEuler(n):
        if MyMath.is_prime(n):
            return n - 1
        div = n - 1
        divs = []
        num = n
        while div > 1 or num > 1:
            if not MyMath.is_prime(div) or num % div != 0:
                div -= 1
                continue
            num = num / div
            divs.append(div)

        euler = 1
        divs = list(set(divs))
        for div in divs:
            euler *= (1 - (1 / div))
        return floor(euler * n)

    @staticmethod
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