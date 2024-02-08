from MyMath import MyMath
from math import gcd


class ComparisonsOfTheFirstDegree(MyMath):

    def _isTotalDiv(self, arr, div):
        for i in arr:
            if i % div != 0:
                return False
        return True

    def comparisonsOfTheFirstDegree(self, a, b, mod):
        print(f"Example: {a}x = {b} mod {mod}")
        xs = 0
        nod = gcd(a, mod)
        print(f"greatest common divisor ===> {nod}")
        valueEuler = MyMath.valueFunctionEuler(mod)
        print(f"value function euler ===> {valueEuler}")
        if nod > 1 and b % nod != 0:
            print("Warning: b % NOD != 0 ! Not solution")
            return None
        if nod > 1 and self._isTotalDiv([a, b, mod], nod):
            a, b, mod = a // nod, b // nod, mod // nod

        countSolution = nod
        if gcd(a, valueEuler) == 1:
            print(f"Solution with theorem euler ===> {a}x={b} mod {mod}")
            # x = (b * pow(a,valueEuler)) % mod
            xs = self._solutionWithTheoremEuler(a, b, mod, valueEuler)
        else:
            print("Solution with Euclidean")
            # s*a+t*b = GCD(a,b)
            s,_,_ = self._extendedEuclideanAlgorithm(a,mod)
            xs = (s*b) % mod

        if xs is None:
            return None
        if countSolution > 1:
            print(" You're lucky! Have some solution")
            xs = [xs]
            for i in range(1, countSolution):
                xs.append(xs[0] + mod * i)
        print("\n")
        return xs

    def _inversionNumbyModule(self, num, mod):
        s, t, g = self._extendedEuclideanAlgorithm(num, mod)
        if g != 1:
            print('multiplicative inversion not exists')
            return None
        print(f"multiplicative inversion {num} = {(s % mod + mod) % mod} ")
        return (s % mod + mod) % mod

    def _solutionWithTheoremEuler(self, a, b, mod, degree):
        degree -= 1

        while degree > 0:
            print(f"x0 = {b}*{a}^{degree} mod {mod}")
            if a == 1:
                break
            if degree % 2 == 0:
                degree = degree / 2
                a *= a
            else:
                b, a = b * a, a * a
                degree = (degree - 1) / 2
            a = self._modulus(a, mod)
            b = self._modulus(b, mod)

        print(f"x0={b} mod {mod}")
        return b

    def _extendedEuclideanAlgorithm(self, a, b):
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

    def _modulus(self, a, mod):
        if a > mod:
            return a % mod
        return a