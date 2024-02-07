from math import gcd
from helper import valueFunctionEuler, extendedEuclideanAlgorithm


def solutionWithTheoremEuler(a, b, mod, degree):
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
        if a > mod:
            a = a % mod
        if b > mod:
            b = b % mod

    print(f"x0={b} mod {mod}")
    return b


# ax+my=b => ax=b mod m
def comparisonsOfTheFirstDegree(a, b, mod):
    xs = 0
    nod = gcd(a, mod)
    print(f"greatest common divisor ===> {nod}")
    valueEuler = valueFunctionEuler(mod)
    print(f"value function euler ===> {valueEuler}")
    if nod > 1 and b % nod != 0:
        print("Warning: b % NOD != 0 ! Not solution")
        return
    if nod > 1 and a % nod == 0 and b % nod == 0 and mod % nod == 0:
        a, b, mod = a // nod, b // nod, mod // nod

    countSolution = nod
    if gcd(a, valueEuler) == 1:
        print(f"Solution with theorem euler ax=b mod m ===> {a}x={b} mod {mod}")
        # x = (b * pow(a,valueEuler)) % mod
        xs = solutionWithTheoremEuler(a, b, mod, valueEuler)
    else:
        print("Solution with Euclidean")
        # x0= (b/d)s y0=(b/d)t
        s, t, g = extendedEuclideanAlgorithm(a, mod)
        if g != 1:
            print("multiplicative inversion not exists")
            return None
        print("multiplicative inversion exists")
        print(f"{(s % mod + mod) % mod} mod {mod}")
        xs = (s % mod + mod) % mod

    if countSolution > 1:
        print(" You're lucky! Have some solution")
        xs = [xs]
        for i in range(1, countSolution):
            xs.append(xs[0] + mod * i)
    return xs


if __name__ == '__main__':
    print(comparisonsOfTheFirstDegree(5, 1, 11))

    # print(extendedEuclideanAlgorithm(21,14))
