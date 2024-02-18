from ChineseRemainderTheorem import ChineseRemainderTheorem
from MyMath import MyMath


class QuadraticResidues(MyMath):

    chineseRemainder = ChineseRemainderTheorem()

    def _symbolJacobi(self, a, p):
        factors = MyMath.factorIntoPrimeFactors(p)
        print(f"Find factors for {p}")
        mult = 1
        if self._isAllDivSame(factors):
            return self._calculateSymbolJacobi(a, factors[0])

        for elem in factors:
            mult = self._calculateSymbolJacobi(a, elem)

            print(f"{a}/{elem} = {mult}; ")
            if mult == 0:
                return 0
        return mult

    def _calculateSymbolJacobi(self, a, elem):
        mult = 1
        if a > elem:
            a = a % elem
        mult *= self.symbolLegandre(a, elem)
        mult = self._reverseClassDeduction(mult, elem)
        return mult

    def symbolLegandre(self, a, p):
        print(f"Find symbol legandre ({a}/{p})")
        a, p = self._divToNOD(a, p)
        if a > p:
            a = a % p
        match a:
            case 0:
                return 0
            case 1:
                return 1
            case 2:
                return pow(-1, ((pow(p, 2) - 1) // 8))
            case -1:
                return pow(-1, (p - 1) // 2)

        if MyMath.is_prime(p) and p % 2 == 1:
            print(f"{p} is prime and odd - execution Euler: a^((p-1)/2) mod p")
            return self._reverseClassDeduction(pow(a, (p - 1) // 2) % p, p)

        if MyMath.isOdd(a) and MyMath.isOdd(p) and MyMath.is_prime(a) and MyMath.is_prime(p):
            return self._reverseClassDeduction(self.symbolLegandre(p % a, a), p) * pow(-1, ((a - 1) * (p - 1)) / 4)

        print(f"Execution Jacobi so as {p} isn't prime and not odd")
        _, _, nod = MyMath.extendedEuclideanAlgorithm(a, p, False)

        if MyMath.isOdd(a) and MyMath.isOdd(p) and nod == 1:
            print(f"NOD({a},{p}) == 1 Execution Jacobi - Gauss ")
            return self._reverseClassDeduction(self.symbolLegandre(p % a, a), p) * pow(-1, ((a - 1) * (p - 1)) / 4)
        else:
            print(f"Execution Jacobi - let's factorize {p}")
            return self._symbolJacobi(a, p)

    # GET = p = 2^h * k + 2^(h-1) + 1 : return h
    def _getDegreeTwoForPrimeNumber(self, a, p):
        if not MyMath.is_prime(p):
            print("P is not prime, you can't use factorization by 2")
            return -1
        k = a
        h = 1
        s = ""
        while k > 0:
            result = pow(2, h) * k + 1

            if result == p:
                s = s + "2^" + str(h) + " * " + str(k) + " + 1="
                h += 1
            if k % 2 == 0:
                k = k // 2
            else:
                k -= 1

        print(s, f"{p}")

        if pow(2, h) * k + (pow(2, h - 1) + 1) == p:
            return h
        else:
            return -1

    def calculateQuadraticResidues(self, a, p):
        print(f"calculate x^2 = {a} mod {p}")
        if a == 1:
            print("Wow! a = 1 , we have solution +-1 mod any")
            return 1

        if not MyMath.isOdd(p) and not MyMath.is_prime(p):
            return self._calcQuadraticResiduesWherePisEven(a, p)
        symbolLegandre = self.symbolLegandre(a, p)
        a = a % p
        match symbolLegandre:
            case 1:
                print(f"Have 2 solution +- L={a}/{p}={symbolLegandre}")
            case -1:
                print(f" Symbol legandre {a}/{p} = -1 ====> not solution")
                return None
            case 0:
                print(f"Have 1 solution: L={a}/{p}={symbolLegandre}")

        if MyMath.is_prime(p):
            print(f"{p} is prime")
            h = self._getDegreeTwoForPrimeNumber(a, p)
            if h != -1:
                x = self._solutionPairsCandidate(a, p, h)
            else:
                print("Sorry,finding is difficult, accept range to 100000")
                x = None
                for i in range(2, 100000):
                    x = i * i % p
                    if x == a:
                        print(f"We found solution with range: x^2={i * i} ===> x=(+-){i} mod {p}")
                        x = i
                        break

            if x is None:
                print("Sorry, we can't find solution")
            return x
        else:
            factors = self.factorIntoPrimeFactors(p)
            print(f"{p} is not prime", [elem for elem in factors])
            if self._isAllDivSame(factors):
                print(f"We have all div same for {p}")
                result = self.calculateQuadraticResidues(a % factors[0], factors[0])
                print(
                    f"Solution: x^2={a} mod {factors[0]} ===> x=+-{result} mod {factors[0]}  ({result}+{factors[0]}t)")
                result = self._calculateT(factors, [result, factors[0]], a)
                print(f"Solution: x=+-({result[0]} mod {p} )")
                return result
            else:
                _, _, nod = MyMath.extendedEuclideanAlgorithm(a, p, False)
                if nod == 1:
                    print(f"NOD({a},{p}) = 1, have solutions")
                    alfa = self._getSeniorDegree(factors)
                    if alfa == 1:
                        count_solutions = pow(2,len(factors))
                    elif alfa == 2:
                        count_solutions = pow(2,len(factors)+1)
                    else:
                        count_solutions = pow(2,len(factors)+2)
                    print("All solutions: =" + str(count_solutions))
                    print("We have next system")
                    system = []
                    for elem in factors:
                        print(f"x^2={a} mod {elem}")
                        system.append([self.calculateQuadraticResidues(count_solutions,elem),elem])
                    system = MyMath.generateSignVariations(system)
                    print(system)
                    solution = []
                    for variation in system:
                        result = self.chineseRemainder.calcChineseRemainder(variation)
                        solution.append(result)
                        print("Solution: " + str(result))
                    return solution






    def _calcQuadraticResiduesWherePisEven(self, a, p):
        if not MyMath.numberIsPowerTwo(p):
            return None
        print("Our mod is power two")
        alfa = MyMath.findPowerTwo(p)
        if alfa == 1:
            print("We have on solution: x=1 mod 2")
            return 1
        elif alfa == 2:
            print("We have two solutions: x=+-1 mod 4")

        print(f"alfa > 3, solution: if {a} = 1 mod 8")
        if a % 8 == 1:
            print(f"{a} = 1 mod 8 ===> have 4 solutions  => x=+-(1+4t)")
            if alfa == 3:
                print("We have solution: +-1 mod 8 and +-3 mod 8")
                return (1, 3)
            factors = [16]
            for i in range(4, alfa):
                factors.append(2)

            result = self._bodyCalculateT(a, [1, 4], factors[0])
            result = self._calculateT(factors, result, a)
            print(f"First solutions: +-({result[0]} mod {p}) second solutions: +-({result[0] + result[1]} mod {p}")
            return result
        return None

    def _calculateT(self, factors, result, a):
        for i in range(1, len(factors)):
            factors[i] = factors[i - 1] * factors[i]
            result = self._bodyCalculateT(a, result, factors[i])
            print("next step")
        return result

    def _bodyCalculateT(self, a, result, currentMod):
        temp = a % currentMod
        print(
            f"({result[0]}+{result[1]}t)^2={result[0] * result[0]}+2*{result[0]}*{result[1]}t*{result[1] * result[1]}t^2"
            f"= {temp} mod {currentMod}")
        temp -= result[0] * result[0]
        t = 2 * result[0] * result[1]
        if temp != 0:
            [temp, t, currentMod] = self._divToNODArray([temp, t, currentMod])
        else:
            t, currentMod = self._divToNOD(t, currentMod)
        if t > currentMod:
            t = t % currentMod
        t = temp // t
        print(f"tprev = {t} mod {currentMod}  ({t}+{currentMod}t)")
        result[0] = result[0] + result[1] * t
        result[1] = result[1] * currentMod
        return result

    def _solutionPairsCandidate(self, a, p, h):
        print(f"pairs of candidate solutions: 2^{h - 2}={pow(2, h - 2)}")
        print(f"Let's find some non-residue modulo {p}")

        someNonResidue = 0
        for i in range(2, p):
            if self.symbolLegandre(i, p) == -1:
                someNonResidue = i
                break
        print(f"We found nonResidue: {someNonResidue}")
        print(f"Using formuls x = {someNonResidue}^(z(2k+1)) * a^(k+1) mod {p}  z=0:{h - 2}")
        for i in range(0, pow(2, h - 2)):
            x = (pow(someNonResidue, i) * a) % p
            print(f"x=(+-){someNonResidue}^{i} * {a} mod {p} ===> {x} ")
            print(f"then: x^2={pow(x, 2) % p} mod {p}")
            if pow(x, 2) % p == a:
                print(f"We found solution: x=(+-){x} mod {p}")
                return x
        return None

    def _isAllDivSame(self, factors):
        total_div = factors[0]
        for div in factors:
            if div != total_div:
                return False
        return True

    def _getSeniorDegree(self,arr):
        max_power = 1
        arr = sorted(arr)
        for i in range(len(arr)):
            power = 1
            for j in range(i+1,len(arr)):
                if arr[i] == arr[j]:
                    power += 1
                if arr[i] != arr[j]:
                    break
            i = j-1
            if power > max_power:
                max_power = power
        return max_power

    def _divToNOD(self, a, b):
        _, _, nod = MyMath.extendedEuclideanAlgorithm(a, b, False)
        return a // nod, b // nod

    def _divToNODArray(self, arr):
        nod = MyMath.gcd_recursiveForArray(arr)
        if nod == 0:
            return arr
        for i in range(len(arr)):
            arr[i] = arr[i] // nod
        return arr

    # Обратное число для класса вычетов 6 % 7 = - 1 % 7
    def _reverseClassDeduction(self, a, b):
        if a + 1 == b:
            return a - b
        return a
