import math
from math import sqrt, floor
from helper import swap
import itertools

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
    def extendedEuclideanAlgorithm(a, b,showStep=True):
        print("Extended Euclidean Algorithm") if showStep is True else None
        s1 = 1
        s2 = 0
        t1 = 0
        t2 = 1
        while a and b:
            q = a // b
            a, b = b, a % b
            s = s1 - q * s2
            s1, s2 = s2, s
            t = t1 - q * t2
            t1, t2 = t2, t
            print(f"q={q}; r1={a}; r2={b}; s1={s1}; s2={s2}; t1={t1}; t2={t2};  s={s};  t={t}") if showStep is True else None
        return s1, t1, a

    @staticmethod
    def isOdd(a):
        return a % 2 == 1

    @staticmethod
    def factorIntoPrimeFactors(n):
        i = 2
        factors = []
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n = n // i
            i = i + 1
        if n > 1:
            factors.append(n)
        return factors

    @staticmethod
    def gcdForArrayNumbers(arr):
        if len(arr) == 2:
            a, b = arr
            _,_,nod = MyMath.extendedEuclideanAlgorithm(a,b,False)
            return nod
        elif len(arr) > 2:
            return MyMath.gcdForArrayNumbers([arr[0], MyMath.gcdForArrayNumbers(arr[1:])])
        else:
            return None

    @staticmethod
    def numberIsPowerTwo(n):
        return n > 0 and (n & (n - 1)) == 0

    @staticmethod
    def findPowerTwo(n):
        if MyMath.numberIsPowerTwo(n):
            power = 0
            while n > 1:
                n //= 2
                power += 1
            return power
        else:
            return None

    @staticmethod
    def generateSignVariations(matrix): #Все вариации знаков (-1,+1)
        rows, cols = len(matrix), len(matrix[0])
        sign_variations = []

        for signs in itertools.product([-1, 1], repeat=rows):
            variation = [matrix[i].copy() for i in range(rows)]
            for i, sign in enumerate(signs):
                variation[i][0] *= sign
            sign_variations.append(variation)

        return sign_variations

    @staticmethod
    def get_bit(num: int, pos: int) -> bool:
        return num >> pos & 1

    @staticmethod
    def shit_bit(num: int, count_shift: int, maxSize: int) -> int:
        return (num << count_shift) % (count_shift << maxSize)

    @staticmethod
    def pollardP1Factorization(n, B):
        a = 2
        e = 2
        while e <= B:
            a = pow(a, e) % n
            e += 1

            p = math.gcd(int(a) - 1, n)
            if 1 < p < n:
                return p
        return -1